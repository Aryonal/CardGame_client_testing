# -*-coding:utf-8-*-
from __future__ import unicode_literals
from models import *

'''
seperate nums, nums seperated by space
nums: str
'''
def seperate_nums(nums):
    lst = nums.split(' ')
    try:
        ns = [int(i) for i in lst]
    except:
        raise InvalidInputError()
    return ns

'''
return True if all items in list1 are in list2
lst1: list[]
lst2: list[]
'''
def list_in_list(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True


if __name__ == '__main__':
    l1 = [1,2,3]
    l2 = [1,3,2,4,5]

    print list_in_list(l1, l2)
