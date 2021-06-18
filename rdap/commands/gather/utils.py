import validators
from .exceptions import (
    DomainWithSubdomain,
    DomainValidationError,
    DomainWithHttp,
)
from rdap.common.utils import (
    get_suffix,
    get_domain,
    get_subdomain,
)


def _has_subdomain(domain:str) -> None:
    """In charge of validate if the domain contains a subdomain

    Args:
        domain (str): [Some domain name. I.e example.com]

    Raises:
        DomainWithSubdomain: [
            Raised when the domain validation regex has found a match
            with a subdomain passed by input with the domain.
        ]
    """
    subdomain = get_subdomain(domain)
    if subdomain:
        raise DomainWithSubdomain(
            (
                "Only admits valid domain names, subdomain are not included. "
                "Try deleting '{0}.' and try again please.".format(
                    domain.split(".")[0]
                )
            )
        )

def _has_http(domain:str) -> None:
    """In charge of validate if the domain contains http or https strings

    Args:
        domain (str): [Some domain name. I.e example.com]

    Raises:
        DomainWithHttp: [
            Raised when the domain validation found http or https
            in the domain input.
        ]
    """

    if "http" in domain:
        raise DomainWithHttp(
            (
                "Only admits valid domain names. "
                "Try deleting '{0}://' and try again please.".format(
                    domain.split("://", 1)[0]
                )
            )
        )

def _regex_domain(domain:str) -> None:
    """In charge of validate if the domain matches with the standart
    domain regex (use of external library - 'Validators')

    Args:
        domain (str): [Some domain name. I.e example.com]

    Raises:
        DomainValidationError: [
            Raised when the domain validation regex does not match
            any coincidence with the domain.
        ]
    """

    if not validators.domain(domain):
        raise DomainValidationError(
            (
                "Only admits valid domain names. "
                "Please try only typing {0}.{1} and try again.".format(
                    get_domain(domain), get_suffix(domain)
                )
            )
        )

def domain_validator(domain:str) -> str:
    """Validator to check if the input domain is valid or not.

    Args:
        domain (str): [Some domain name. I.e example.com]

    Returns:
        str: [return back the domain if it is all ok]
    """
    _has_http(domain)
    _has_subdomain(domain)
    _regex_domain(domain)
    
    return domain
