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
        return temp.value
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length-=1
        return temp.value
    


my_linkedlist = DoublyLinkedlist(0)
my_linkedlist.append(1)
my_linkedlist.append(2)
print(my_linkedlist.remove(1))
my_linkedlist.print_list()