from sys import path
path.append('../../modules')

from os import strerror
from debugA import bprint

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    errno = 1

class FileEmpty(StudentsDataException):
    errno = 2

#Read file
filename = input("Student notes source file: ") + '.txt'
bprint(filename)
try:
    src = open(filename, 'r')
except IOError as e:
    print("Couldn't open file: \'" + filename + '\': ', strerror(e.errno))

def total(file):
    line = file.readline()
    if not line:
        raise FileEmpty
    students = {}
    while line:
        splt = list(line.split())
        if len(splt) != 3:
            raise BadLine
        if (splt[0], splt[1]) in students.keys():
            students[(splt[0], splt[1])] += float(splt[2])
        else:
            students[(splt[0], splt[1])] = float(splt[2])
        
        line = file.readline()

    return students


def foo(a):
    return a

try:
    scores = total(src)
    sort = input("Sort by last name? ")
    names = list(scores.keys())
    if sort:
        sort = 1
    else:
        sort = 0
    names.sort(key=lambda a: a[sort])
    
    max = 0
    for i in names:
        if (length := len(i[0]) + len(i[1])) > max:
            max = length
    
    for i in range(max+11):
        print('-', end='')
    print()

    print("Student", end='')
    for i in range(max-2):
        print(' ', end='')
    print("Points", end='\n')

    for i in range(max+11):
        print('-', end='')
    print()

    for i in names:
        length = len(i[0]) + len(i[1])
        if sort:
            print(i[1] + ', ' + i[0], end='')
            for j in range(max-length+3):
                print(' ', end='')
            print(scores[i])
        else:
            print(i[0] + ' ' + i[1], end='')
            for j in range(max-length+3):
                print(' ', end='')
            print(scores[i])
        print()

except FileEmpty as e:
    print("Sorry, the file is empty.")
    exit(e.errno)
except BadLine as e:
    print("Sorry, the input file contained a line in the wrong format.\nPlease amend and try again.")
    exit(e.errno)
