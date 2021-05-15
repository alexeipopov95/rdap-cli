import click
import json
import dateutil.parser
from datetime import datetime

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

def _load_file_data(filename:str) -> dict:
    """receive a file name and return as a dict
    Args:
        filename (str): [filename]
    Returns:
        dict: [return a dict object]
    """

    with open(filename, "r") as output:
        data = json.load(output)
    return data

def _save_file_data(data:dict, filename:str) -> None:
    """Save data in a file

    Args:
        data (dict): [data to be saved]
        filename (str): [filename where data is going to be saved]
    """

    with open(filename, "w") as input:
        json.dump(data, input)

def _string_to_datetime(date:str) -> datetime:
    return dateutil.parser.parse(date).replace(tzinfo=None)
