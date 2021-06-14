from os import error


class DomainValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        


class DomainWithSubdomain(DomainValidationError):
    pass


class DomainWithHttp(DomainValidationError):
    pass


class DomainRegexDoesNotMatch(DomainValidationError):
    pass
