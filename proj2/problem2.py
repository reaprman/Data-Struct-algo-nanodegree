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
    files = []
    #files = os.listdir(path)
    try:
      for filename in os.listdir(path):
        if os.path.isdir(path+"/"+filename):
          files.extend(find_files(suffix, path+"/"+filename))
        if filename.endswith(suffix,len(filename)-3):
          files.append(filename)
    except:
      print("No path provided")
      return
    return files

## Locally save and call this file ex.py ##
# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print(os.listdir("."))

# Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))
print(find_files(".c", "./testdir"))
print(find_files(".c", ""))
print(find_files(".exe","./testdir"))