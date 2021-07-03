class DomainValidationError(Exception):
    """
    Raised when the domain validation regex does not match
    any coincidence with the domain.
    """

    def __init__(self, message):
        super().__init__(message)


class DomainWithSubdomain(DomainValidationError):
    """
    Raised when the domain validation regex has found a match
    with a subdomain passed by input with the domain.
    """


class DomainWithHttp(DomainValidationError):
    """
    Raised when the domain validation found http or https
    in the domain input.
    """
