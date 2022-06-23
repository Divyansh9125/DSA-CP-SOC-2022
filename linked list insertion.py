from asyncio.windows_events import NULL

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
    
    def insertatend(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next

t = int(input())
llist = LinkedList()
for i in range(t):
    n,x = map(int,input().split())
    if (x==0):
        llist.insertatbegin(n)
    else:
        llist.insertatend(n)

llist.printList()


