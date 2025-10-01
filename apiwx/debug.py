'''
# Api wxPython debug logger
'''
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
    def __init__(self, logger_name: str, log_dir: str, log_timestamp: str, log_tag_length: int, log_maxline: int, log_maxfiles: int, log_level: LogLevel = LogLevel.DEBUG):
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
    # loop daemon thread
        while(True):
            # has log message ?
            if(self._buffer):
                # get log message
                message = self._buffer.pop(0)
                # print log message
                self._logprint(message)
                # save log message
                self._logsave(message)
            else:
                # wait idle signal
                self._log_idlesignal.wait()
                # clear idle signal
                self._log_idlesignal.clear()


    def _logprint(self, message: str):
        # end with linefeed ?
        if message.endswith("\n"):
            # remove linefeed (print is add linefeed default)
            message = message[0:len(message) - 1]
            
        # flush: print just now
        print(message, flush = True)


    def _logsave(self, message: str):
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

                    with open(self._log_dir + f"\\{self._name}.log", "r") as logfile:
                        line_amount = len(logfile.readlines())

                    if(line_amount >= self._log_maxline):
                        os.rename(
                            self._log_dir
                            + f"\\{self._name}.log",
                            self._log_dir
                            + f"\\{self._name + datetime.now().strftime('%Y%m%d%H%M%S')}.log"
                        )

                except:
                    ...

                # file add mode
                with open(self._log_dir + f"\\{self._name}.log", "a") as logfile:
                    # write lines
                    logfile.write(message)


    def log(self, tag: str, message: str, level: LogLevel = LogLevel.INFO):
        """Log a message with specified level"""
        # Check if this level should be logged
        if level < self._log_level:
            return

        # Format level string
        level_str = level.to_string().ljust(8)[0:8].upper()

        # add log message to buffer
        self._buffer.append(
            f"{
                self._get_time_stamp()
            } [{
                self._name.ljust(self._log_tag_length)[
                    0:self._log_tag_length
                ].upper()
            }] [{
                level_str
            }] [{
                tag.ljust(self._log_tag_length)[
                    0:self._log_tag_length
                ].upper()
            }] {
                message
            }"
        )

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


def create_logger_from_sysargs(option: uiarg.Options, name: str) -> Logger | None:
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