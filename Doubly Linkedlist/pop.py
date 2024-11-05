class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail  # Link the new node's prev to the current tail
            self.tail.next = new_node  # Link the current tail's next to the new node
            self.tail = new_node       # Update the tail to be the new node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  # Move the tail pointer back
            self.tail.next = None       # Set the new tail's next to None
            temp.prev = None            # Clean up temp's prev reference
        self.length -= 1
        return temp.value  # Return the value of the popped node

# Testing the updated code
my_linkedlist = DoublyLinkedlist(1)
my_linkedlist.append(2)
print(my_linkedlist.pop())  # Expected output: 2
print(my_linkedlist.pop())  # Expected output: 1
print(my_linkedlist.pop())  # Expected output: None (since the list is now empty