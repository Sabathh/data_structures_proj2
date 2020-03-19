class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def list_to_set(llist : LinkedList) -> set:
    """ Converts a LinkedList into a set.
        Traverses the entire list. Time complexity of O(n)
    
    Arguments:
        llist {LinkedList} -- LinkedList
    Returns:
        set -- Set containing all elements of llist
    """
    current_node = llist.head
    lset = set()
    while current_node is not None:
        lset.add(current_node.value)
        current_node = current_node.next
    
    return lset


def union(llist_1 : LinkedList, llist_2 : LinkedList) -> LinkedList:
    """ Uses sets to generate a LinkedList containing the union of llist_1 and llist_2

        Time complexity is defined by the for loops, which depends on the size of both sets. 
        O(n), where n is len(llist_1) + len(llist_2)

        Space complexity scales linearly with the size of the lists: O(n)

    Arguments:
        llist_1 {LinkedList} -- LinkedList object
        llist_2 {LinkedList} -- LinkedList object
    
    Returns:
        LinkedList -- LinkedList containing the union of inputs
    """
    # Convert to set to remove repeated entries in each list
    lset_1 = list_to_set(llist_1)
    lset_2 = list_to_set(llist_2)
    
    # Combine the two sets to create a union
    union_list = LinkedList()
    list_of_added = []
    for item in lset_1:
        union_list.append(item)
        list_of_added.append(item)

    for item in lset_2:
        if item not in list_of_added:
            union_list.append(item)

    return union_list

def intersection(llist_1 : LinkedList, llist_2 : LinkedList) -> LinkedList:
    """ Uses sets to generate a LinkedList containing the intersection of llist_1 and llist_2

        Time complexity is defined by the for loops, which depends on the size of both sets. 
        O(n), where n is len(llist_1) + len(llist_2)

        Space complexity scales linearly with the size of the lists: O(n)

    Arguments:
        llist_1 {LinkedList} -- LinkedList object
        llist_2 {LinkedList} -- LinkedList object
    
    Returns:
        LinkedList -- LinkedList containing the intersection of inputs
    """
    # Convert to set to remove repeated entries in each list
    lset_1 = list_to_set(llist_1)
    lset_2 = list_to_set(llist_2)

    # Initialize empty intersec_list
    intersec_list = LinkedList()
    
    # Populate list_of_candidates with all elements from lset_1
    list_of_candidates = []
    for item in lset_1:
        list_of_candidates.append(item)

    # Only add to intersec_list the items from lset_2 available in list_of_candidates
    for item in lset_2:
        if item in list_of_candidates:
            intersec_list.append(item)

    return intersec_list

def test_edge_cases():
    pass

def test_standard_lists(element_1 : list, element_2 : list):

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    union_list = union(linked_list_1,linked_list_2)
    intersec_list = intersection(linked_list_1,linked_list_2)

    node = union_list.head
    if node is None:
        # Triggered when both lists are empty
        assert(len(element_1) == 0 and len(element_2) == 0)
    else:
        while node is not None:
            assert(node.value in element_1+element_2)
            node = node.next

    node = intersec_list.head
    if node is None:
        # Triggered when intersection is empty
        intersec_set = set(element_1).intersection(set(element_2))
        assert(len(intersec_set) == 0)
    else:
        while node is not None:
            assert(node.value in element_1 and node.value in element_2)
            node = node.next

if __name__ == "__main__":
    test_edge_cases()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    test_standard_lists(element_1, element_2)

    element_3 = [3,2,4,35,6,65,6,4,3,23]
    element_4 = [1,7,8,9,11,21,1]
    test_standard_lists(element_3, element_4)

    element_5 = []
    element_6 = []
    test_standard_lists(element_5, element_6)


