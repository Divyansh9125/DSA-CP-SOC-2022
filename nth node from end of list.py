class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize

class LinkedList:
    def __init__(self):
        self.head = None

    def insertatbegin(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
    
    def nodefromend(self,n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        
        if n > length:
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)

t = int(input())
u = int(input())
llist = LinkedList()
for i in range(t):
    llist.insertatbegin(int(input()))
print(llist.nodefromend(u))
