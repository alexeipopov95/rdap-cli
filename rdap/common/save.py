import os
import click
from typing import Any
from rdap.common.utils import save_file_data
from rdap.common.constants import (
    MessageColors,
    TextFormatConstants,
)
from rdap.common.exceptions import NotSupportedFileFormat


class Save:
    FILE_TYPE = None
    AVAILABLE_EXTENCION = (
        TextFormatConstants.JSON,
        TextFormatConstants.TEXT,
    )

    @classmethod
    def _validate_format(cls, filename: str) -> type:
        """Validate if the fileformat is supported by the CLI.

        Args:
            filename (str): [Filename. I.e myfile.json]

        Raises:
            NotSupportedFileFormat: [
                Raised when the CLI found a non supported file format.
            ]
        """
        extention = filename.split(".", 1)[1]
        if not filename.endswith(cls.AVAILABLE_EXTENCION):
            raise NotSupportedFileFormat(
                f"The fileformat [{extention}] is not supported yet."
            )
        cls.FILE_TYPE = extention

    @classmethod
    def save_harvest(cls, filename: str, content: Any):
        """Save the content into the filename if the file format
        is supported.

        Args:
            filename (str): [Filename. I.e myfile.json]
            content (Any): [The content to be saved.]
        """

        try:
            cls._validate_format(filename)
        except NotSupportedFileFormat as ex:
            return click.echo(
                click.style(f"[ERROR] - {ex}", fg=MessageColors.RED, bold=True)
            )

        save_file_data(
            content,
            filename,
            cls.FILE_TYPE,
        )

        return click.echo(
            click.style(
                f"[DONE] - File saved successfully in {os.getcwd()}/{filename}",
                fg=MessageColors.GREEN,
                bold=True,
            )
        )
