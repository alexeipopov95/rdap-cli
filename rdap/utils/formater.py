import click
from rdap.common.constants import FormatterStatus as STATUS
from rdap.common.constants import MessageColors as COLORS


def formater(
    message:str,
    status:str=STATUS.INFO,
    color:str=COLORS.WHITE
) -> None:
    """function designed to format dinamically the 
    output messages for every case it needs

    Args:
        message (str): [the notifcation or the error message]
        status (str, optional): [status of the output
        the values can be info, error, success or debug]. Defaults to STATUS.INFO.
        color (str, optional): [Just color]. Defaults to COLORS.WHITE.
    """
