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


def is_user_in_group(user : str, group : Group) -> bool:
    """Return True if user is in the group, False otherwise.
    
    Arguments:
        user {str} -- user name/id
        group {Group} -- group to check user membership against
    
    Returns:
        bool -- True if user is in the group, False otherwise.
    """
    if user in group.get_users():
        # User is in group
        return True
    elif len(group.get_groups()) > 0:
        # Check if user is in any of the subgroups
        for elem in group.get_groups():
            if is_user_in_group(user, elem):
                return True
    return False

def test_edge_cases():
    
    null_group = Group(None) # Group name is not used
    assert(is_user_in_group("orphan", null_group) == False)

    single_group = Group("single_parent")
    single_child = "single_child"
    single_group.add_user(single_child)
    assert(is_user_in_group(single_child, single_group) == True)
    assert(is_user_in_group("sibling", single_group) == False)
    assert(is_user_in_group(None, single_group) == False)


def test_standard_group():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    assert(is_user_in_group(sub_child_user, sub_child) == True)

    assert(is_user_in_group(sub_child_user, child) == True)

    assert(is_user_in_group(sub_child_user, parent) == True)

    assert(is_user_in_group("orphan", parent) == False)

def test_big_group():

    grandparent = Group("grandpa")
    parent = Group("parent")
    first_child = Group("first_child")
    second_child = Group("second_child")

    kid_1 = "kid_1"
    kid_2 = "kid_2"
    kid_3 = "kid_3"
    kid_4 = "kid_4"

    grandparent.add_group(parent)
    parent.add_group(first_child)
    parent.add_group(second_child)

    first_child.add_user(kid_1)
    first_child.add_user(kid_2)

    second_child.add_user(kid_3)
    second_child.add_user(kid_4)

    assert(is_user_in_group(kid_1, grandparent) == True)
    assert(is_user_in_group(kid_2, grandparent) == True)
    assert(is_user_in_group(kid_3, grandparent) == True)
    assert(is_user_in_group(kid_4, grandparent) == True)

    assert(is_user_in_group(kid_1, parent) == True)
    assert(is_user_in_group(kid_2, parent) == True)
    assert(is_user_in_group(kid_3, parent) == True)
    assert(is_user_in_group(kid_4, parent) == True)

    assert(is_user_in_group(kid_1, first_child) == True)
    assert(is_user_in_group(kid_2, first_child) == True)
    assert(is_user_in_group(kid_3, first_child) == False)
    assert(is_user_in_group(kid_4, first_child) == False)

    assert(is_user_in_group(kid_1, second_child) == False)
    assert(is_user_in_group(kid_2, second_child) == False)
    assert(is_user_in_group(kid_3, second_child) == True)
    assert(is_user_in_group(kid_4, second_child) == True)

    assert(is_user_in_group("orphan", grandparent) == False)
    assert(is_user_in_group("orphan", parent) == False)
    assert(is_user_in_group("orphan", first_child) == False)
    assert(is_user_in_group("orphan", second_child) == False)



if __name__ == "__main__":
    
    test_edge_cases()

    test_standard_group()

    test_big_group()