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

def huffman_encoding(data : str):
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
    freq_list = sorted(freq_list, key = lambda x: -x.value[1])
    guide_list = [(k, v) for k, v in freq_dict.items()]
    guide_list = sorted(guide_list, key = lambda x: -x[1])

    # Assemble Huffman Tree
    huffman_tree = Tree()

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
    
    def traverse(node, string, huffman_dict):
        if not node.has_left_child() and not node.has_right_child():
            node.value = node.value[0]
            if string == "":
                string = "0" # If data is a single char
            huffman_dict[node.value] = string
            return

        if node is not None:
            traverse(node.left, string + "0", huffman_dict)
            traverse(node.right, string + "1", huffman_dict)

    traverse(huffman_tree.root, "", huffman_dict)

    # Encode input

    encoded_str = ""
    for char in data:
        encoded_str += huffman_dict[char]

    return encoded_str, huffman_tree


def huffman_decoding(data,tree):
    # Decode

    curr_node = tree.root
    
    decoded_str = ""
    for item in data:
        if item == "0":
            curr_node = curr_node.left
        elif item == "1":
            curr_node = curr_node.right

        # If node is a leaf, retrieve char
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
    