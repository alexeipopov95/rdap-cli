class GatherCommandError(Exception):
    pass


class GatherEmptyParam(GatherCommandError):
    def __init__(self, msg):
        super().__init__(msg)


class GatherInvalidDomainName(GatherCommandError):
        def __init__(self, msg):
            super().__init__(msg)