'''
# Api wxPython argument parser
'''
import sys
import enum


class Options(enum.Enum):
    UI_DEBUG = '--ui-debug'
    _INTERNAL_LOG = '--internal-log'


def exist_option(option: Options) -> int:
    return option.value in sys.argv


def get_option(option: Options) -> list[str]:
    option_list = sys.argv[
        sys.argv.index(option.value) : len(sys.argv)
    ]

    for other in Options:
        if other.value in option_list:
            if other == option:
                continue
            
            option_list = (
                option_list[
                    0: option_list.index(
                        other.value
                    )
                ]
            )

    return option_list


def get_var(option_list: str, varname: str):
    for option_var in option_list:
        if varname in option_var:
            return option_var.replace(f"{varname}=", "")

    return None