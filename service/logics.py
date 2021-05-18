from user.models import Role


def add_service_user_role(user):
    role_dict = {}
    user.roles.clear()
    role = Role.objects.filter(name='service_user').first()
    user.roles.add(role)
    role_dict['id'] = role.id
    role_dict['name'] = role.name
    role_dict['status'] = role.status
    return role_dict
