class MessageColors:
    BLACK = "black"
    GREEN = "green"
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    CYAN = "cyan"
    WHITE = "white"


class RdapDomainEvents:
    REGISTRATION = "registration"
    EXPIRATION = "expiration"
    LAST_CHANGED = "last changed"
    LAST_CHANGED_RDAP = "last update of RDAP database"


class TextFormatConstants:
    TEXT = "txt"
    JSON = "json"


class DomainAvailability:
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"

    availability_color_map = {
        AVAILABLE : MessageColors.GREEN,
        UNAVAILABLE : MessageColors.RED
    }