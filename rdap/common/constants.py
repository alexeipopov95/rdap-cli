
class DomainStatus:
    REGISTRATED = "REGISTRATED"
    AVAILABLE = "AVAILABLE"


class MessageColors:
    BLACK = "black"
    GREEN = "green"
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    CYAN = "cyan"
    WHITE = "white"


class FormatterStatus:
    INFO = "INFO"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"
    DEBUG = "DEBUG"


class RdapDomainEvents:
    REGISTRATION = "registration"
    EXPIRATION = "expiration"
    LAST_CHANGED = "last changed"
    LAST_CHANGED_RDAP = "last update of RDAP database"