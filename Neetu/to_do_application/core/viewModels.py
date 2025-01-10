from dataclasses import dataclass, fields, field
from core.enums import PriorityEnum, StatusEnum
from datetime import datetime


@dataclass
# it provided you some features that set the value you passed while creating instance in the variables of the dataclass
# also make them instance variable
# these variable are called Fields
class TaskVM:
    # instance variable
    title: str
    description: str
    _priority: PriorityEnum
    status: StatusEnum = field(default=StatusEnum.PENDING)
    time: str = field(default=datetime.now().strftime("%H:%M:%S"))


    def __post_init__(self):
        for field in fields(TaskVM):
            expectedtype = field.type

            if not isinstance(getattr(self, field.name), expectedtype):
                raise TypeError("`%s` must be %s" % (field.name, expectedtype))

    @property
    def priority(self):
        return self._priority.name
