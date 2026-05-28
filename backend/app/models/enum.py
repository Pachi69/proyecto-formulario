from enum import Enum


class FormType(str, Enum):
    REGISTER = "Register"
    UNREGISTER = "Unregister"

class Status(str, Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


