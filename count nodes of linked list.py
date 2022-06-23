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

    def countNodes(self):
        count = 0
        temp = self.head
        while (temp is not None):
            count = count + 1
            temp = temp.next
        
        return count

n = int(input())
llist = LinkedList()
for i in range (n):
    llist.push(int(input()))
    

        

    
