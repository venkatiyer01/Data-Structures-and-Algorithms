"""You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Note: this linked list class does NOT have a tail which will make this method easier to implement.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the remove_duplicates() method in two different ways:



Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.



Here is the method signature you need to implement:

def remove_duplicates(self):


Example:

Input:

LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

Output:

LinkedList: 1 -> 2 -> 3 -> 4 -> 5

"""

#Solution:

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
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def remove_duplicates(self):
        if self.head is None:
            return None
        current = self.head
        seen_values = set()
        seen_values.add(current.value)
        while current.next is not None:
            if current.next.value in seen_values:
                current.next = current.next.next
            else:
                seen_values.add(current.next.value)
                current = current.next

            
my_linkedlist = Linkedlist(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(1)
my_linkedlist.append(4)
my_linkedlist.append(2)
my_linkedlist.append(5)
my_linkedlist.remove_duplicates()
my_linkedlist.print_list()
    
