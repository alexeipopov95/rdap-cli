class SaveCommandError(Exception):
    pass


class NotSupportedFormat(SaveCommandError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FileReadError(Exception):
    pass


class ImproperlyConfiguredFile(FileReadError):
    def __init__(self, msg):
        super().__init__(msg)
