import random


def producecode():
    str_list = '1230456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    code = ''
    for i in range(4):
        code += random.choice(str_list)
    return code
