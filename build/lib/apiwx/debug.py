"""Debug logging system for apiwx framework.

This module provides a comprehensive logging system designed specifically for 
the apiwx framework. It includes threaded logging capabilities, configurable
log levels, file rotation, and both UI debug and internal logging systems.

The module features:
- Multi-threaded logging with buffered message processing
- Configurable log levels from DEBUG to CRITICAL
- Automatic log file rotation based on size and count limits
- Separate loggers for UI debugging and internal framework logging
- Command-line argument integration for logger configuration

Classes:
    LogLevel: Enum defining log severity levels
    Logger: Thread-based logger with file output and rotation

Functions:
    Various logging convenience functions for UI and internal logging

Example:
    from apiwx.debug import uilog, LogLevel
    
    uilog("NETWORK", "Connection established", LogLevel.INFO)
    uilog("ERROR", "Failed to load config", LogLevel.ERROR)

Note:
    The logger system automatically starts daemon threads for asynchronous
    log processing. Loggers are configured via command-line arguments using
    the uiarg module.
"""
import os.path
import threading
from datetime import datetime
from enum import IntEnum


try:
    from . import uiarg

except ImportError:
    import uiarg


class LogLevel(IntEnum):
    """Log levels in ascending order of severity"""
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    @classmethod
    def from_string(cls, level_str: str) -> 'LogLevel':
        """Convert string to LogLevel"""
        level_map = {
            'DEBUG': cls.DEBUG,
            'INFO': cls.INFO,
            'WARNING': cls.WARNING,
            'ERROR': cls.ERROR,
            'CRITICAL': cls.CRITICAL,
            # Aliases
            'WARN': cls.WARNING,
            'CRIT': cls.CRITICAL,
        }

        return level_map.get(level_str.upper(), cls.DEBUG)

    def to_string(self) -> str:
        """Convert LogLevel to string"""
        level_names = {
            self.DEBUG: 'DEBUG',
            self.INFO: 'INFO',
            self.WARNING: 'WARNING',
            self.ERROR: 'ERROR',
            self.CRITICAL: 'CRITICAL',
        }

        return level_names.get(self, 'DEBUG')


class Logger(threading.Thread):
    """Thread-based logger with file output and rotation capabilities.
    
    This class implements a daemon thread that processes log messages
    asynchronously. It supports configurable log levels, automatic file
    rotation based on line count and file count limits, and both console
    and file output.
    
    The logger maintains an internal buffer of messages and processes them
    in a separate thread to avoid blocking the main application thread.
    
    Args:
        logger_name: Name identifier for the logger thread
        log_dir: Directory path where log files will be stored
        log_timestamp: strftime format string for timestamp formatting
        log_tag_length: Maximum length for log tags (truncated if longer)
        log_maxline: Maximum lines per log file before rotation
        log_maxfiles: Maximum number of log files to keep
        log_level: Minimum log level threshold for output
        
    Attributes:
        _buffer: Internal message buffer for thread-safe logging
        _log_dir: Directory path for log file storage
        _log_timestamp: Timestamp format string
        _log_tag_length: Maximum tag display length
        _log_maxline: Line limit per file
        _log_maxfiles: File count limit
        _log_level: Minimum logging threshold
        _log_idlesignal: Threading event for message processing
        
    Example:
        logger = Logger("MyApp", "./logs", "%Y-%m-%d %H:%M:%S", 
                       8, 5000, 10, LogLevel.INFO)
        logger.info("INIT", "Application started")
    """


    def __init__(
            self,
            logger_name: str,
            log_dir: str,
            log_timestamp: str,
            log_tag_length: int,
            log_maxline: int,
            log_maxfiles: int,
            log_level: LogLevel = LogLevel.DEBUG):
        """Initialize the logger thread with configuration parameters.
        
        Sets up the logger thread as a daemon thread and initializes all
        configuration parameters. The logger thread starts immediately
        upon initialization.
        """
        # init thread
        super().__init__(
            target = self._logger,
            name = logger_name,
            # if exit from main thread,
            # exit from this thread
            daemon = True
        )

        # create log buffer
        self._buffer = []

        # save logging path
        self._log_dir = log_dir

        # log timestamp format (for strftime)
        self._log_timestamp = log_timestamp

        # tag max length
        self._log_tag_length = log_tag_length

        # log max line
        self._log_maxline = log_maxline

        # log max files
        self._log_maxfiles = log_maxfiles

        # minimum log level to output
        self._log_level = log_level

        # logger thread idle signal
        self._log_idlesignal = threading.Event()

        # start log thread
        self.start()


    def _logger(self):
        """Main logger thread loop for processing buffered messages."""
        # Daemon thread main loop
        while True:
            # Process messages if available
            if self._buffer:
                message = self._buffer.pop(0)
                self._logprint(message)
                self._logsave(message)
            else:
                # Wait for new messages
                self._log_idlesignal.wait()
                self._log_idlesignal.clear()


    def _logprint(self, message: str):
        """Print log message to console, handling newline normalization."""
        # Remove trailing newline if present (print adds its own)
        if message.endswith("\n"):
            message = message[:-1]
            
        # Print immediately with flush
        print(message, flush=True)


    def _logsave(self, message: str):
        """Save log message to file with rotation management.
        
        Handles file writing with automatic rotation based on line count
        and maximum file count limits. Creates log directory if needed
        and manages old file cleanup.
        """
        # exists log folder
        if os.path.exists(self._log_dir):
            # if endline is not linefeed ?
            if not message.endswith("\n"):
                # add linefeed
                message += "\n"

                line_amount = 0

                try:
                    logfiles = os.listdir(self._log_dir)

                    if(len(logfiles) >= self._log_maxfiles):
                        os.remove(
                            f"{self._log_dir}\\{sorted(logfiles)[1]}"
                        )

                    log_file_path = os.path.join(
                        self._log_dir, f"{self._name}.log"
                    )
                    with open(log_file_path, "r") as logfile:
                        line_amount = len(logfile.readlines())

                    if(line_amount >= self._log_maxline):
                        current_log = os.path.join(
                            self._log_dir, f"{self._name}.log"
                        )
                        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                        archived_log = os.path.join(
                            self._log_dir, 
                            f"{self._name}{timestamp}.log"
                        )
                        os.rename(current_log, archived_log)

                except:
                    ...

                # file add mode
                log_file_path = os.path.join(
                    self._log_dir, f"{self._name}.log"
                )
                with open(log_file_path, "a") as logfile:
                    # write lines
                    logfile.write(message)


    def log(self, tag: str, message: str, level: LogLevel = LogLevel.INFO):
        """Log a message with specified level and tag.
        
        Adds a log message to the internal buffer for processing by the
        logger thread. The message will only be logged if the specified
        level meets or exceeds the logger's minimum log level threshold.
        
        The logged message includes a timestamp, logger name, tag, and
        the actual message content, all properly formatted for output.
        
        Args:
            tag: A category or context identifier for the message.
            message: The actual log message content.
            level: The severity level of the message (default: INFO).
                  
        Example:
            logger.log("NETWORK", "Connection established", LogLevel.INFO)
            logger.log("ERROR", "Failed to load config", LogLevel.ERROR)
        """
        # Check if this level should be logged
        if level < self._log_level:
            return

        # Format log components
        timestamp = self._get_time_stamp()
        logger_tag = self._name.ljust(self._log_tag_length)
        logger_tag = logger_tag[0:self._log_tag_length].upper()
        message_tag = tag.ljust(self._log_tag_length)
        message_tag = message_tag[0:self._log_tag_length].upper()
        
        # add log message to buffer
        formatted_message = (
            f"{timestamp} [{logger_tag}] [{message_tag}] {message}"
        )
        self._buffer.append(formatted_message)

        # call signal
        self._log_idlesignal.set()


    def debug(self, tag: str, message: str):
        """Log debug message"""
        self.log(tag, message, LogLevel.DEBUG)


    def info(self, tag: str, message: str):
        """Log info message"""
        self.log(tag, message, LogLevel.INFO)


    def warning(self, tag: str, message: str):
        """Log warning message"""
        self.log(tag, message, LogLevel.WARNING)


    def error(self, tag: str, message: str):
        """Log error message"""
        self.log(tag, message, LogLevel.ERROR)


    def critical(self, tag: str, message: str):
        """Log critical message"""
        self.log(tag, message, LogLevel.CRITICAL)


    def set_level(self, level: LogLevel):
        """Change the minimum log level"""
        self._log_level = level


    def get_level(self) -> LogLevel:
        """Get current minimum log level"""
        return self._log_level


    def _get_time_stamp(self):
        return datetime.now().strftime(
            self._log_timestamp
        )


def create_logger_from_sysargs(
        option: uiarg.Options, 
        name: str) -> Logger | None:
    """Create a Logger instance from system command-line arguments.
    
    Parses command-line arguments to extract logger configuration and
    creates a Logger instance with the specified parameters. Returns
    None if the required option is not present in the arguments.
    
    Args:
        option: The uiarg.Options enum value to check for
        name: Name identifier for the logger
        
    Returns:
        Configured Logger instance or None if option not found
        
    Example:
        logger = create_logger_from_sysargs(
            uiarg.Options.UI_DEBUG, "ui_logger"
        )
    """
    if uiarg.exist_option(option):
        options = uiarg.get_option(
            option
        )

        log_dir = uiarg.get_var(options, 'log_dir')

        if log_dir is None:
            log_dir = ".\\log" # default log dir

        log_timestamp = uiarg.get_var(options, 'log_timestamp')

        if log_timestamp is None:
            log_timestamp = "%Y/%m/%d %H:%M:%S"

        log_tag_length = uiarg.get_var(options, 'log_tag_length')

        if log_tag_length is None:
            log_tag_length = 8

        log_maxline = uiarg.get_var(options, 'log_maxline')

        if log_maxline is None:
            log_maxline = 5000

        log_maxfiles = uiarg.get_var(options, 'log_maxfiles')

        if log_maxfiles is None:
            log_maxfiles = 10

        log_level_str = uiarg.get_var(options, 'log_level')

        if log_level_str is None:
            log_level = LogLevel.DEBUG # Default to lowest level

        else:
            log_level = LogLevel.from_string(log_level_str)

        return Logger(
            name,
            log_dir,
            log_timestamp,
            log_tag_length,
            log_maxline,
            log_maxfiles,
            log_level
        )
    
    return None


def remain_logger_output(logger: Logger | None):
    """Process any remaining messages in the logger buffer.
    
    Forces the logger to process all remaining buffered messages
    before shutdown. Waits up to 1 second for message processing
    to complete, then manually processes any remaining messages.
    
    Args:
        logger: Logger instance to flush, or None (no-op)
    """
    if logger is not None:

        logger._log_idlesignal.clear()

        logger._log_idlesignal.wait(1) # wait max 1 seconds

        while(logger._buffer):
            # get log message
            message = logger._buffer.pop(0)
            # print log message
            logger._logprint(message)
            # save log message
            logger._logsave(message)


uidebug = create_logger_from_sysargs(uiarg.Options.UI_DEBUG, "uidebug")

internal = create_logger_from_sysargs(uiarg.Options._INTERNAL_LOG, "internal")


def uilog(tag: str, message: str, level: LogLevel = LogLevel.INFO):
    """Log a message to UI debug logger"""
    if uidebug is not None:
        uidebug.log(tag, message, level)


def uidebug_log(tag: str, message: str):
    """Log debug message to UI debug logger"""
    uilog(tag, message, LogLevel.DEBUG)


def uiinfo_log(tag: str, message: str):
    """Log info message to UI debug logger"""
    uilog(tag, message, LogLevel.INFO)


def uiwarning_log(tag: str, message: str):
    """Log warning message to UI debug logger"""
    uilog(tag, message, LogLevel.WARNING)


def uierror_log(tag: str, message: str):
    """Log error message to UI debug logger"""
    uilog(tag, message, LogLevel.ERROR)


def uicritical_log(tag: str, message: str):
    """Log critical message to UI debug logger"""
    uilog(tag, message, LogLevel.CRITICAL)


def uidebug_set_level(level: LogLevel):
    """Set UI debug logger level"""
    if uidebug is not None:
        uidebug.set_level(level)


def uidebug_get_level() -> LogLevel:
    """Get UI debug logger level"""
    if uidebug is not None:
        return uidebug.get_level()
    
    return LogLevel.DEBUG


def uilog_output_remaining():
    remain_logger_output(uidebug)


def internallog(tag: str, message: str, level: LogLevel = LogLevel.INFO):
    """Log a message to internal logger"""
    if internal is not None:
        internal.log(tag, message, level)


def internaldebug_log(tag: str, message: str):
    """Log debug message to internal logger"""
    internallog(tag, message, LogLevel.DEBUG)


def internalinfo_log(tag: str, message: str):
    """Log info message to internal logger"""
    internallog(tag, message, LogLevel.INFO)


def internalwarning_log(tag: str, message: str):
    """Log warning message to internal logger"""
    internallog(tag, message, LogLevel.WARNING)


def internalerror_log(tag: str, message: str):
    """Log error message to internal logger"""
    internallog(tag, message, LogLevel.ERROR)


def internalcritical_log(tag: str, message: str):
    """Log critical message to internal logger"""
    internallog(tag, message, LogLevel.CRITICAL)


def internal_set_level(level: LogLevel):
    """Set internal logger level"""
    if internal is not None:
        internal.set_level(level)


def internal_get_level() -> LogLevel:
    """Get internal logger level"""
    if internal is not None:
        return internal.get_level()
    
    return LogLevel.DEBUG


def internallog_output_remaining():
    remain_logger_output(internal)


__all__ = [
    # Core classes
    'LogLevel',
    'Logger',
    
    # Logger creation and management
    'create_logger_from_sysargs',
    'remain_logger_output',
    
    # UI Debug logging functions
    'uilog',
    'uidebug_log',
    'uiinfo_log', 
    'uiwarning_log',
    'uierror_log',
    'uicritical_log',
    'uidebug_set_level',
    'uidebug_get_level',
    'uilog_output_remaining',
    
    # Internal logging functions
    'internallog',
    'internaldebug_log',
    'internalinfo_log',
    'internalwarning_log', 
    'internalerror_log',
    'internalcritical_log',
    'internal_set_level',
    'internal_get_level',
    'internallog_output_remaining',
    
    # Logger instances
    'uidebug',
    'internal',
]