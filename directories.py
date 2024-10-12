from sys import path
path.append("./modules")
from debugA import bprint
import os

"""
os.makedirs("./tree/c/other_courses/cpp")
os.makedirs("./tree/c/other_courses/python")
os.makedirs("./tree/cpp/other_courses/c")
os.makedirs("./tree/cpp/other_courses/python")
os.makedirs("./tree/python/other_courses/c")
os.makedirs("./tree/python/other_courses/cpp")
"""

def find(path, dir):
    ret_list = []
    os.chdir(path)
    dirlist = os.listdir()
    
    bprint("Showing dirlist for: " + os.getcwd())
    for t in dirlist:
        bprint("->" + t)
    bprint('')
    
    for y in dirlist:
        if y.lower() == dir.lower():
            ret_list.append(os.getcwd())
            ret_list += find('./' + y, dir)
        else:
            try:
                ret_list += find(os.getcwd() + '\\' + y, dir)
            except NotADirectoryError:
                continue
            except PermissionError:
                os.chdir('../')
            except FileNotFoundError:
                os.chdir('../')
                raise
    bprint("^Back up 1")
    os.chdir('../')
    return ret_list

dir = input("Directory name to find: ")
found = find("C:/Users/arula/Documents", dir)


found.sort(key=lambda a: len(a.split('\\')))

print(f"Found {dir} in")
[print(i) for i in found]

