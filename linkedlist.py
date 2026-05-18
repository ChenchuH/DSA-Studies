'''
A linked list is a set of elements where each element points to its next element. It is useful when you want to frequently add or remove data inside the list itself.
In a regular indexed list, adding an item to the middle is like a queue at a grocery store: you have to shift everyone in line back one spot to make room for the new person. 
In a linked list, it is like a chain where you can simply break one link, insert a new link, and reconnect them without moving anything else.
Linked lists are also useful because they grow dynamically, meaning they don't require you to guess and pre-allocate a large block of memory ahead of time. 
Finally, they are great for creating explicit pointer relationships between data objects rather than relying strictly on numerical index positions.

'''
'''
important to note, these are not good for random access, data needs to traverse to a given point. Ex. arr[500] is fast but if you were to look into that in a linked list if would need to traverse through all points to get to the 500th term. 
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

print(node1.data)

print(node1.next.data)

print(node1.next.next.data)