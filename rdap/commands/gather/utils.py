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
    _has_http(domain)
    _has_subdomain(domain)
    _regex_domain(domain)
    
    return domain