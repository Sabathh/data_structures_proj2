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

 # /TODO: Add more testcases



def is_user_in_group(user, group) -> bool:
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    elif len(group.groups) > 0:
        for elem in group.groups:
            if is_user_in_group(user, elem):
                return True
    return False

if __name__ == "__main__":
    
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    is_user_in_group(sub_child_user, sub_child)

    is_user_in_group(sub_child_user, child)

    is_user_in_group(sub_child_user, parent)