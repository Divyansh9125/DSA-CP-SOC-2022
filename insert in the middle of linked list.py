class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertinmiddle(self,x):
        if (self.head == None):
            self.head = Node(x)
 
        else:
            newNode = Node(x)
            slow = self.head
            fast = self.head.next
 
            while (fast != None and
                   fast.next != None):
                slow = slow.next
                fast = fast.next.next
 
            newNode.next = slow.next
            slow.next = newNode
    
    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end = " "),
            temp = temp.next
    
n = int(input())
llist = LinkedList()
for i in range (n):
    llist.push(int(input()))

p = int(input())

llist.insertinmiddle(p)
llist.display()
 




