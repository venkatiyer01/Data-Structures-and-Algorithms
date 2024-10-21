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
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
            
            
my_linkedlist = Linkedlist(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)
my_linkedlist.reverse()
my_linkedlist.print_list()
    
