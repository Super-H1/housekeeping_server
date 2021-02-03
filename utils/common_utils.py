import random


def producecode():
    str_list = '1230456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    code = ''
    for i in range(4):
        code += random.choice(str_list)
    return code


def get_model_fields(obj, related_name=None, remove_list=None, add_list=None):
    # obj_name = obj.__name__
    # r = obj.__doc__.replace('' + obj_name + '(', '').replace(')', '')
    # print(r)
    # lists = r.split(',')
    # lists = [l.strip() for l in lists]
    fields = obj._meta.fields
    lists = [field.name for field in fields]
    if remove_list is not None:
        if type(remove_list) is list:
            [lists.remove(l) for l in remove_list]
    if add_list is not None:
        if type(add_list) is list:
            for l in add_list:
                lists.append(l)
    if related_name is not None:
        lists.append(related_name)
    return lists