# !/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
   def __init__(self, node_data):
       self.data = node_data
       self.next = None

class SinglyLinkedList:
   def __init__(self):
       self.head = None
       self.tail = None

   def insert_node(self, node_data):
       node = SinglyLinkedListNode(node_data)

       if not self.head:
           self.head = node
       else:
           self.tail.next = node

       self.tail = node

def print_singly_linked_list(node, sep = " "):
   while node:
       print(str(node.data))

       node = node.next




#
# Complete the 'removeNodes' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST listHead
#  2. INTEGER x
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeNodes(listHead, x):
    # Write your code here
    """
    this code copies into a list and then copies the same into another listhead and return it.
    Working = True
    :param listHead: 
    :param x: 
    :return: 
    """
    node = listHead
    i = 0
    prev_node = listHead
    new_head = SinglyLinkedList()
    l = []
    while node:
        if node.data <= x:
            l.append(node.data)
        node = node.next
    for i in range(0, len(l)):
        new_head.insert_node(l[i])
    return new_head.head

def real_remove_Nodes(listHead, x):
    """
    deletes nodes having their data attribute less than x.
    working = True
    :param listHead: 
    :param x: 
    :return: 
    """
    node = listHead.next
    prev_node = listHead
    while node.next:
        if node.data > x:
            print("ok boi")
            prev_node.next = node.next
            # prev_node = node.next
            node = node.next
            print("prev", prev_node.data)
            print("node", node.data)
        else:
            prev_node = node
            node = node.next
    if node.data > x:
        print("you were wrong")
        print("prev", prev_node.data)
        print("node", node.data)
        prev_node.next = None
    #removing head if it's not alright!
    if listHead.data > x:
        print("removed head boi", listHead.data)
        listHead = listHead.next
    return listHead



# if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    listHead_count = int(input().strip())
#
#    listHead = SinglyLinkedList()
#
#    for _ in range(listHead_count):
#        listHead_item = int(input().strip())
#        listHead.insert_node(listHead_item)
#
#    x = int(input().strip())
#
#    result = removeNodes(listHead.head, x)
#
#    print_singly_linked_list(result, '\n', fptr)
#    fptr.write('\n')
#
#    fptr.close()


# taking input

listHead_count = int(raw_input().strip())

listHead  = SinglyLinkedList()

for i in range(listHead_count):
    listHead_item = int(raw_input().strip())
    listHead.insert_node(listHead_item)
x = int(raw_input().strip())
result = real_remove_Nodes(listHead.head, x)
print_singly_linked_list(result, " ")
