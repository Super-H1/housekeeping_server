from enum import Enum


class OrderStatus(Enum):
    Unpaid = 0
    AdminCheck = 11
    Paid = 10
    Evaluation = 20
    PaidFailed = 30
