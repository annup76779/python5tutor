from enum import StrEnum, IntEnum


class PriorityEnum(StrEnum):
    SEVERE = 's'
    MEDIUM = 'm'
    LOW = 'l'


class StatusEnum(IntEnum):
    FAILED = 2
    COMPLETED = 1
    PENDING = 0
