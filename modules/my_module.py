#!/usr/bin/env python3 

"""my excercise python module"""

__counter = 0;

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for item in the_list:
        the_sum += item
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for item in the_list:
        prod *= item
    return prod

if __name__ == "__main__":
    print("I prefer to be imported, but I am running myself")
    my_list = [i + 1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
