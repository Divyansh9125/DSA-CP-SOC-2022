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
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
    
    def mergeList(self,head1,head2):
        dummynode = Node(0)
        tail = Node(0)
        while True:
            if head1 is None:
                tail.next = head2
                break
            if head2 is None:
                tail.next = head1
                break
            if head1 <= head2:
                tail.next = head1
                head1 = head1.next
            
            else:
                tail.next = head2
                head2 = head2.next
            
            tail = tail.next
        
        return dummynode.next
    
listA = LinkedList()
listB = LinkedList()
n = int(input())
m = int(input())

for i in range (n):
    listA.push(int(input()))
for j in range (m):
    listB.push(int(input()))
 
# Call the merge function
listA.head = mergeList(listA.head,listB.head)
listA.printList()


