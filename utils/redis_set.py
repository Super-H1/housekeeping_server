# redis配置

from django_redis import get_redis_connection

Res = get_redis_connection()

phone = Res.get('15501632071')
print(phone)