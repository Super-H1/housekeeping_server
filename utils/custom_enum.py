from enum import Enum


class OrderStatus(Enum):
    Unpaid = 0
    AdminCheck = 11  # 管理员确认付款状态
    Paid = 10  # 已付款
    Evaluation = 20
    PaidFailed = 30
    Accept = 40  # 已接单
    Refuse = 41  # 已拒绝
    Refund = 42  # 退款中
    ServiceComplete = 50  # 服务人员确认订单完成
    UserOrderComplete = 60  # 用户确认订单完成
    OrderRefundSuccess = 70  # 退款成功
    ComplainOrder = 80 # 投诉订单
