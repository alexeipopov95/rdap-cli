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

    formater_color_map = {
        INFO : MessageColors.YELLOW,
        ERROR : MessageColors.RED,
        SUCCESS : MessageColors.GREEN,
        DEBUG : MessageColors.WHITE,
    }


class RdapDomainEvents:
    REGISTRATION = "registration"
    EXPIRATION = "expiration"
    LAST_CHANGED = "last changed"
    LAST_CHANGED_RDAP = "last update of RDAP database"


class TextFormatConstants:
    TEXT = "txt"
    JSON = "json"
    CSV = "csv"
    YML = "yml"

class DomainAvailability:
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"

    availability_color_map = {
        AVAILABLE : MessageColors.GREEN,
        UNAVAILABLE : MessageColors.RED
    }