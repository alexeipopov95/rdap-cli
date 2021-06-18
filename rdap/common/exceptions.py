class SaveCommandError(Exception):
    pass


class NotSupportedFormat(SaveCommandError):
    """
    This exception occurs when the user entersa text
    format that is not valid or is not supported by the cli.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
