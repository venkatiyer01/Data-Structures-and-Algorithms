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
    def swap_first_last(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return None
        else:
            self.head.value,self.tail.value = self.tail.value,self.head.value
                      
my_linkedlist = DoublyLinkedlist(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.swap_first_last()
my_linkedlist.print_list()                    