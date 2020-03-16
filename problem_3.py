import sys

class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

    @property
    def left(self) -> 'Node':
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self) -> 'Node':
        return self._right

    @right.setter
    def right(self, node : 'Node'):
        self._right = node

    @property
    def value(self) -> 'Node':
        return self._value

    @value.setter
    def value(self, node : 'Node'):
        self._value = node

    def has_left_child(self) -> bool:
        return self.left != None

    def has_right_child(self) -> bool:
        return self.right != None

class Tree():
    def __init__(self, value=None ):
        self._root = Node(value)
        
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node : Node):
        self._root = node

def huffman_encoding(data : str) -> (str, Tree):
    """ Encodes data using a Huffman Tree. 
        Code complexity is O(n*log(n)) due to assembling the tree 
        and usage of the sorted() and traverse() functions
    Arguments:
        data {str} -- Data to be encoded
    
    Returns:
        [str, Tree] -- Encoded data in a binary string, Huffman Tree used in the encoding
    """
    # If no data is provided return empty tree
    if len(data) == 0:
        return "", Tree()

    # Determine frequency of each letter
    freq_dict = {}
    for letter in data:
        if letter in freq_dict.keys():
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    
    # Convert dict into list of tuples
    freq_list = [Node((k, v)) for k, v in freq_dict.items()]
    freq_list = sorted(freq_list, key = lambda x: -x.value[1]) # sorted is O(n*log(n))

    # Assemble Huffman Tree
    huffman_tree = Tree()

    # Each letter takes O(log(n)) to be inserted into the tree. 
    # Assembling the entire tree then takes O(n*log(n))
    while len(freq_list) > 1:
        left_node = freq_list.pop()
        right_node = freq_list.pop()
        new_node = Node((left_node.value[0] + right_node.value[0],left_node.value[1] + right_node.value[1]))

        new_node.left = left_node
        new_node.right = right_node
        
        next_iter = False
        for index in range(0, len(freq_list)):
            if freq_list[index].value[1] == new_node.value[1]:
                freq_list.insert(index, new_node)
                next_iter = True
                break

        if next_iter:
            continue
        else:
            freq_list.append(new_node)

    huffman_tree.root = freq_list[0]

    if not huffman_tree.root.has_left_child() and not huffman_tree.root.has_right_child():
        root_node = Node(huffman_tree.root.value)
        root_node.left = huffman_tree.root
        root_node.right = huffman_tree.root
        huffman_tree.root = root_node

    # Traverse tree to generate dictionary
    huffman_dict = {}
    
    def traverse(node : Node, string : str, huffman_dict : dict):
        """ Traverses tree from starting node and assembles a string 
            that defines a path on the tree leading to a specific leaf. 
            0 = go down the left node
            1 = go down the right node

            The final string for each leaf is added to a dictionary 

            Since it takes O(log(n)) to reach an individual leaf the
            total time complexity is O(n*log(n)).
        
        Arguments:
            node {node} -- First node of a tree
            string {str} -- Contains the path to reach a specific leaf of the tree
            huffman_dict {dict} -- Dictionary that will store the paths to all the leaves in the tree
        """
        # Base case: Leaf has been found. Add string to dictionary
        if not node.has_left_child() and not node.has_right_child():
            node.value = node.value[0]
            if string == "":
                string = "0" # If data is a single char
            huffman_dict[node.value] = string
            return

        if node is not None:
            # Not a leaf. Continue traversing the tree
            traverse(node.left, string + "0", huffman_dict)
            traverse(node.right, string + "1", huffman_dict)

    traverse(huffman_tree.root, "", huffman_dict)

    # Encode input using the assembled huffman_dict
    encoded_str = ""
    for char in data:
        encoded_str += huffman_dict[char]

    return encoded_str, huffman_tree


def huffman_decoding(data : str, tree : Tree) -> str:
    """ Decodes data in binary string format using a Huffman Tree.
        Since the data containg the path used to traverse the tree
        no tree search is required to decode. Complexity of O(n).
    
    Arguments:
        data {str} -- String containing data in binary format. Is used to locate elements in the tree
        tree {Tree} -- Huffman Tree used to decode data
    
    Returns:
        str -- Decoded data in string format
    """
    # Decode
    curr_node = tree.root
    
    decoded_str = ""
    # Uses data to traverse tree. 
    # 0 = go down left. 1 = go down right
    for item in data:
        if item == "0":
            curr_node = curr_node.left
        elif item == "1":
            curr_node = curr_node.right

        # If node is a leaf, retrieve char and return to root of tree
        if not curr_node.has_left_child() and not curr_node.has_right_child():
            decoded_str += curr_node.value
            curr_node = tree.root
                
    return decoded_str
    
def test_huffman(data : str):
    print("===========================================================")
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)
    if data is not "": # Size of encoded data only printed when there is data to encode
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    assert(decoded_data == data)

if __name__ == "__main__":
    codes = {}

    # Empty string
    test_huffman("")

    # Single value string
    test_huffman("B")

    # A great sentence
    test_huffman("The bird is the word")

    # An even greater sentence
    test_huffman("A-well-a everybody's heard about the bird! Bird bird bird, b-bird's the word!")
    