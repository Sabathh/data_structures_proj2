import warnings

class Node:
    def __init__(self, key=None, value=None):
        self._key = key
        self._value = value
        self.next = None
        self.prev = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

class DoublyLinkedList:
    """ Doubly Linked List to be used to track the usage of
        items in the LRU Cache. 
        A Doubly Linked List Data Structure was prefered due to the following:
            -   O(1) to remove a known node. All it takes is connecting previous node to next node. 
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, node : Node):
        """ Prepend a node to the beginning of the list. 
        
        Arguments:
            node {Node} -- Node to be added to the head of the list
        """
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head # Add node before current head node
            self.head.prev = node 
            self.head = node      # Set node as head node
    
    def remove(self, node: Node):
        """ Removes node from list by connecting previous and next nodes directly to each other
        
        Arguments:
            node {Node} -- Node to be removed from list
        """
        previous_node = node.prev
        next_node = node.next
        if previous_node is None and next_node is None:
            self.head = None
            self.tail = None
        elif node == self.tail:
            previous_node.next = None
            self.tail = previous_node
        elif node == self.head:
            next_node.prev = None
            self.head = next_node
        else:
            previous_node.next = next_node
            next_node.prev = previous_node


class LRU_Cache(object):
    """ LRU_Cache uses a dictionary to store data and Doubly Linked List for usage tracking.
        Dictionary is O(1) for both storage and retriaval of data
        Doubly Linked List is O(1) for both removing and prepending nodes.
    """
    def __init__(self, capacity : int):
        # Initialize class variables
        self._cache_dict = {}
        if capacity < 1:
            warnings.warn("Specified capacity lower than 1. Setting cache capacity to 1.", Warning)
            self._capacity = 1
        else:
            self._capacity = capacity

        self._lru_list = DoublyLinkedList() # DoublyLinkedList to track recent usage of items in cache 

    def get(self, key):
        """ Retrieve item from provided key. 
            Updates DoublyLinkedList that keeps track of cache usage
        
        Arguments:
            key {[type]} -- Key used to find item stored in cache
        
        Returns:
            Node.value -- Value stored in cache. Return -1 if nonexistent.
        """
        if key in self._cache_dict.keys():
            retrieved_node = self._cache_dict[key]

            # Move used node to head of DoublyLinkedList
            self._lru_list.remove(retrieved_node)
            self._lru_list.prepend(retrieved_node)

            return retrieved_node.value
        else:
            return -1

    def set(self, key, value):
        """ Set the value if the key is not present in the cache. 
            If the cache is at capacity remove the oldest item.
            The oldest item is either the last one inserted or the last one accessed.
        
        Arguments:
            key {[type]} -- Key used to store value stored in cache
            value {[type]} -- Value to be stored in cache
        """
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self._cache_dict) < self._capacity:
            self._cache_dict[key] = Node(key, value)
            self._lru_list.prepend(self._cache_dict[key])
        else:
            oldest_node = self._lru_list.tail # Least used item is always at the end of the DoublyLinkedList

            # Removes node from both dictionary and DoublyLinkedList
            old_key = oldest_node.key
            del self._cache_dict[old_key]
            self._lru_list.remove(oldest_node)

            # Adds new value to dictionary and to the head of DoublyLinkedList
            self._cache_dict[key] = Node(key, value)
            self._lru_list.prepend(self._cache_dict[key])
        

def test_complete_lrc_cache():

    our_cache = LRU_Cache(5)
    
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    
    assert(our_cache.get(1) == 1)       # returns 1
    assert(our_cache.get(2) == 2)       # returns 2
    assert(our_cache.get(9) == -1)      # returns -1 because 9 is not present in the cache
    
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    
    assert(our_cache.get(3) == -1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

def test_edge_cases():
    null_cache = LRU_Cache(0) # If the capacity provided is lower than 1 then the capacity will be set to 1.

    # Add single value
    null_cache.set(1, 1)
    assert(null_cache.get(1) == 1)

    # Replace value using same key
    null_cache.set(1, 2)
    assert(null_cache.get(1) == 2)

    # Replace key and value
    null_cache.set(2, 2)
    assert(null_cache.get(1) == -1)
    assert(null_cache.get(2) == 2)

def test_lrc_cache_operations():
    # Create cache with 10 positions
    big_cache = LRU_Cache(10)

    # Add 10 items
    big_cache.set(0, 0)
    big_cache.set(1, 1)
    big_cache.set(2, 2)
    big_cache.set(3, 3)
    big_cache.set(4, 4)
    big_cache.set(5, 5)
    big_cache.set(6, 6)
    big_cache.set(7, 7)
    big_cache.set(8, 8)
    big_cache.set(9, 9)

    # Assert 10 items
    assert(big_cache.get(0) == 0)
    assert(big_cache.get(1) == 1)
    assert(big_cache.get(2) == 2)
    assert(big_cache.get(3) == 3)
    assert(big_cache.get(4) == 4)
    assert(big_cache.get(5) == 5)
    assert(big_cache.get(6) == 6)
    assert(big_cache.get(7) == 7)
    assert(big_cache.get(8) == 8)
    assert(big_cache.get(9) == 9)

    # Assert invalid items
    assert(big_cache.get(42) == -1)
    assert(big_cache.get(666) == -1)

    # Replace last used item
    big_cache.set(42, 42)
    assert(big_cache.get(0) == -1)
    assert(big_cache.get(42) == 42)

    # Re-set (1, 1) so (2, 2) becomes the last used item. Then, replace it
    big_cache.set(1, 1)
    big_cache.set(666, 666)
    assert(big_cache.get(2) == -1)
    assert(big_cache.get(1) == 1)
    assert(big_cache.get(666) == 666)

if __name__ == "__main__":

    test_edge_cases()

    test_complete_lrc_cache()

    test_lrc_cache_operations()


