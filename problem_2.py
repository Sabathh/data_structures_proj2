import os
from typing import List

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_files = []

    recursive_find_files(suffix, path, list_of_files)

    return list_of_files

def recursive_find_files(suffix : str, path : str, list_of_files : List[str]):
  """ Recursively find files containing suffix and append to list_of_files. 
      All folders/files are verified only once. O(n)
  
  Arguments:
      suffix {str} -- File extension 
      path {str} -- Path of directory/file to be searched
      list_of_files {List[str]} -- List of strings that shall contain the result
  """
  # Base case: If a path to a file is provided, return
  if os.path.isfile(path):
    if path.endswith(suffix):
      list_of_files.append(path)
    return

  # If directory path is provided then call recursive_find_files once for each item in directory
  for item in os.listdir(path):
    item_path = os.path.join(path, item)
    recursive_find_files(suffix, item_path, list_of_files)

def test_find_files():
  # Single folder containing one file to be found
  assert(find_files(".c", ".\\problem_2_dir\\subdir1") == ['.\\problem_2_dir\\subdir1\\a.c'])
  # Single folder containing no file to be found
  assert(find_files(".c", ".\\problem_2_dir\\subdir2") == [])
  # Deep path containing multiple files to be found
  assert(find_files(".c", ".\\problem_2_dir\\deepdir") == ['.\\problem_2_dir\\deepdir\\deepdir1\\deepdir1_1\\deepdir1_1_1\\a.c',
                                                           '.\\problem_2_dir\\deepdir\\deepdir1\\deepdir1_1\\deepdir1_1_1\\b.c',
                                                           '.\\problem_2_dir\\deepdir\\deepdir1\\deepdir1_1\\deepdir1_1_1\\c.c'])
  # Full test
  assert(find_files(".c", ".\\problem_2_dir") == ['.\\problem_2_dir\\deepdir\\deepdir1\\deepdir1_1\\deepdir1_1_1\\a.c',
                                                  '.\\problem_2_dir\\deepdir\\deepdir1\\deepdir1_1\\deepdir1_1_1\\b.c',
                                                  '.\\problem_2_dir\\deepdir\\deepdir1\\deepdir1_1\\deepdir1_1_1\\c.c',
                                                  '.\\problem_2_dir\\subdir1\\a.c', 
                                                  '.\\problem_2_dir\\subdir3\\subsubdir1\\b.c', 
                                                  '.\\problem_2_dir\\subdir5\\a.c',
                                                  '.\\problem_2_dir\\t1.c'])

if __name__ == "__main__":
  
  test_find_files()

  print("Tests completed!")

