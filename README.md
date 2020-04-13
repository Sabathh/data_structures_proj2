# Data Structures & Algorithms Nanodegree Program (Udacity)

Note: The following text was assembled using parts of the original descriptions available in the Nanodegree ND256 at the time of writing. For more information about the Nanodegree please visit the official page [here](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256).

## Project 2: Show Me the Data Structures

Table of Contents

- [Data Structures & Algorithms Nanodegree Program (Udacity)](#data-structures--algorithms-nanodegree-program-udacity)
  - [Project 2: Show Me the Data Structures](#project-2-show-me-the-data-structures)
    - [Description](#description)
    - [Problem 1 - Least Recently Used Cache](#problem-1---least-recently-used-cache)
    - [Problem 2 - File Recursion](#problem-2---file-recursion)
    - [Problem 3 - Huffman Coding](#problem-3---huffman-coding)
      - [Resources](#resources)
    - [Problem 4 - Active Directory](#problem-4---active-directory)
    - [Problem 5 - Blockchain](#problem-5---blockchain)
    - [Problem 6 - Union and Intersection](#problem-6---union-and-intersection)

### Description

For this project, you will answer the six questions laid out in the next sections. The questions cover a variety of topics related to the data structures you've learned in this course. You will write up a clean and efficient answer in Python, as well as a text explanation of the efficiency of your code and your design choices.

### Problem 1 - Least Recently Used Cache

The lookup operation (i.e., `get()`) and `put()` / `set()` is supposed to be fast for a cache memory.

While doing the `get()` operation, if the entry is found in the cache, it is known as a `cache hit`. If, however, the entry is not found, it is known as a `cache miss`.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the `put()` operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an `use operation`.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a `cache hit`, your `get()` operation should return the appropriate value.
In case of a `cache miss`, your `get()` should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take `O(1)` time.

For the current problem, you can consider the `size of cache = 5`.

_The solution of problem 1 can be found [here](https://github.com/Sabathh/data_structures_proj2/blob/master/problem_1.py)._

### Problem 2 - File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

The directory tree used for this can be found [here](https://github.com/Sabathh/data_structures_proj2/tree/master/problem_2_dir).

Python's `os` module will be useful—in particular, you may want to use the following resources:

[os.path.isdir(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isdir)
[os.path.isfile(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isfile)
[os.listdir(directory)](https://docs.python.org/3.7/library/os.html#os.listdir)
[os.path.join(...)](https://docs.python.org/3.7/library/os.path.html#os.path.join)

**Note:** `os.walk()` is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use `os.walk()`.

_The solution of problem 2 can be found [here](https://github.com/Sabathh/data_structures_proj2/blob/master/problem_2.py)._

### Problem 3 - Huffman Coding

A **Huffman code** is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

- Take a string and determine the relevant frequencies of the characters.
- Build and sort a list of tuples from lowest to highest frequencies.
- Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
- Trim the Huffman Tree (remove the frequencies from the previously built tree).
- Encode the text into its compressed form.
- Decode the text from its compressed form.

_The solution of problem 3 can be found [here](https://github.com/Sabathh/data_structures_proj2/blob/master/problem_3.py)._

#### Resources

[Huffman Visualization!](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)
[Tree Generator](http://huffman.ooz.ie/)
[Additional Explanation](https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html)

### Problem 4 - Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

``` python
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
```

Write a function that provides an efficient look up of whether the user is in a group.

_The solution of problem 4 can be found [here](https://github.com/Sabathh/data_structures_proj2/blob/master/problem_4.py)._

### Problem 5 - Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

_The solution of problem 5 can be found [here](https://github.com/Sabathh/data_structures_proj2/blob/master/problem_5.py)._

### Problem 6 - Union and Intersection

Fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

Take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once the problem is completed create own test cases and perform a run time analysis on the code.

_The solution of problem 6 can be found [here](https://github.com/Sabathh/data_structures_proj2/blob/master/problem_6.py)._

