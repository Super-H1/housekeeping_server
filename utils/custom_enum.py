from enum import Enum


class OrderStatus(Enum):
    Unpaid = 0
    Paid = 10
    Evaluation = 20
    PaidFailed = 30
