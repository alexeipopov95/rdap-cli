from rdap.common.utils import save_file_data
from typing import Any
import click
from rdap.common.constants import (
    MessageColors,
    TextFormatConstants,
)
from rdap.commands.gather.exceptions import (
    NotSupportedFileFormat
)

class Save:
    AVAILABLE_EXTENCION = (
        TextFormatConstants.JSON,
        TextFormatConstants.TEXT,
    )
    FILE_TYPE = None

    @classmethod
    def _validate_format(cls, filename:str) -> type:
        extention = filename.split('.',1)[1]
        if not filename.endswith(cls.AVAILABLE_EXTENCION):
            raise NotSupportedFileFormat(
                f"The fileformat [{extention}] is not supported yet."
            )
        cls.FILE_TYPE = extention

    @classmethod
    def save_harvest(cls, filename:str, content:Any):
        try:
            cls._validate_format(filename)
        except NotSupportedFileFormat as ex:
            return click.echo(
                click.style(
                    f"[ERROR] - {ex}",
                    fg=MessageColors.RED,
                    bold=True
                )
            )
        
        if cls.FILE_TYPE == TextFormatConstants.JSON:
            save_file_data(
                content,
                filename,
                TextFormatConstants.JSON,
            )
        elif cls.FILE_TYPE == TextFormatConstants.TEXT:
            save_file_data(
                content,
                filename,
                TextFormatConstants.TEXT,
            )

        # TODO: Return the path where the file was saved.
        return click.echo(
            click.style(
                "[DONE] - File saved successfully.",
                fg=MessageColors.GREEN,
                bold=True,
            )
        )




