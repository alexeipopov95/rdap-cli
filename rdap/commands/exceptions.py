class GatherCommandError(Exception):
    pass


class GatherEmptyParam(GatherCommandError):
    def __init__(self, msg):
        super().__init__(msg)


class GatherInvalidDomainName(GatherCommandError):
    def __init__(self, msg):
        super().__init__(msg)


class SaveCommandError(Exception):
    pass


class NotSupportedFormat(SaveCommandError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)