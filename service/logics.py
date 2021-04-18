from user.models import Role


def add_service_user_role(user):
    user.roles.clear()
    role = Role.objects.filter(name='service_user').first()
    user.roles.add(role)
    return role
