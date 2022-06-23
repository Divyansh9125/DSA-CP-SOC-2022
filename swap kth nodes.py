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
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count

    def swap(self,k):
        n = self.countNodes()
        if k>n:
            return
        if (2 * k - 1) == n:
            return

        #kth node from start
        x = self.head
        x_prev = Node(None)
        for i in range(k - 1):
            x_prev = x
            x = x.next
 
        #kth node from end
        y = self.head
        y_prev = Node(None)
        for i in range(n - k):
            y_prev = y
            y = y.next
        
        if x_prev is not None:
            x_prev.next = y
        if y_prev is not None:
            y_prev.next = x
        
        temp = x.next
        x.next = y.next
        y.next = temp

        if k == 1:
            self.head = y
        if k == n:
            self.head = x

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,"")
            temp = temp.next

llist = LinkedList()
t = int(input())
for i in range(t):
    llist.push(int(input()))
llist.swap(int(input()))
llist.printlist()


