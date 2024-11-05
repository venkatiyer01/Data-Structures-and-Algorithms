class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return True              
my_linkedlist = DoublyLinkedlist(1)
my_linkedlist.append(2)
my_linkedlist.prepend(3)
my_linkedlist.print_list()                        