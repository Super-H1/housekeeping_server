from order.models import OrderService
from reward.models import Reward
from user.models import UserInfo


def add_reward_to_user(instance):
    '''
    发放赏金
    :return:
    '''
    # 查询改订单对应的服务
    queries = OrderService.objects.filter(order=instance).all()
    for query in queries:
        # 查询该服务对应的用户
        service = query.service
        user = UserInfo.objects.filter(service=service).first()
        # 添加赏金记录
        reward, _ = Reward.objects.update_or_create(user=user)
        reward.money += float('{:>.2f}'.format(instance.price * 0.1))
        reward.is_grant = False
        reward.save()
        if reward.total_money - service.grade * 1500 >= 1500:
            service.grade += 1
            service.save()
