"""Question - LL: Find Middle Node ( ** Interview Question)
Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop.
"""

#Solution :- 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1            
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
my_linked_list = Linkedlist(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)        