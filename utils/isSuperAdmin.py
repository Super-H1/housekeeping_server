from user.models import Permission, Role


def isSuperAdmin(userId):
    permissions = Permission.objects.filter(code=100000).first()
    if not permissions:
        return False

    roles = Role.objects.filter(permissions=permissions, status=EnableStatus.normal.value, userinfo__id=userId).all()
    if not roles:
        return False
    return True