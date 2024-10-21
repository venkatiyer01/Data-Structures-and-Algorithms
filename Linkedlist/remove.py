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
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.tail = None
        return temp
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length-=1
        return temp
            

my_linkedlist = Linkedlist(11)
my_linkedlist.append(3)
my_linkedlist.append(23)
my_linkedlist.append(7)
print(my_linkedlist.remove(3),'\n')
my_linkedlist.print_list()

