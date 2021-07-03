class FileError(Exception):
    def __init__(self, message):
        super().__init__(message)


class FileDoesNotExist(FileError):
    """
    This exception is raised when the file is not found.
    """


class NotSupportedFileFormat(FileError):
    """
    Raised when the CLI found a non supported file format.
    """
