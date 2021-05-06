def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    curr_group = group
    users = curr_group.get_users()
    if not users:
        groups = curr_group.get_groups()
        for i in range(len(groups)):
            return is_user_in_group(user, groups[i])
    else:
        if user in users:
            return True
    return False

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

if is_user_in_group(sub_child_user, parent):
    print("User is in group")
else:
    print("User Not in group")

