from django.contrib.auth.models import User, Permission, Group, ContentType

# create user
u4 = User()
u4.username = 'user4'
u4.set_password('connordburge')
u4.save()

# create permissions
content_type = ContentType.objects.get_for_model(User)
p = Permission()
p.name = 'My Edit Perm'
p.codename = 'my_edit_perm'
p.content_type = content_type
p.save()

# create group
g = Group()
g.name = 'Editor'
g.save()
g.permissions.add(p)

# add group to user
u4.groups.add(g)
