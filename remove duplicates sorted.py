class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,"")
            temp = temp.next

    def removeDuplicates(self):
        if self.head is None or self.head.next is None:
            return
        
        hash = set()
        current = self.head
        hash.add(current.data)
 
        while current.next is not None:
 
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
    
n = int(input())
llist = LinkedList()
for i in range (n):
    llist.push(int(input()))
llist.removeDuplicates()
llist.printlist()
        
