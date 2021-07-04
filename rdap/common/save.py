import os
from typing import Any
from rdap.common.utils import save_file_data, formater
from rdap.common.constants import TextFormatConstants, AlertTagMessage
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

        try:
            extention = filename.split(".", 1)[1]
        except IndexError:
            raise NotSupportedFileFormat("Invalid file format.")

        if not filename.endswith(cls.AVAILABLE_EXTENCION):
            raise NotSupportedFileFormat(
                f"The fileformat [{extention}] is not supported."
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
            return formater(
                ex,
                AlertTagMessage.ERROR,
            )

        save_file_data(
            content,
            filename,
            cls.FILE_TYPE,
        )
        return formater(
            f"File successfully saved to {os.getcwd()}/{filename}",
            AlertTagMessage.DONE,
        )
