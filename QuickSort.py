class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution(Node):
    def __init__(self):
        self.head = None
    def insertAtBegin(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            newnode.next = self.head
    def insertAtEnd(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end ="-->")
            temp = temp.next
        print(None)
    def getTail(self,node):
        while node and node.next:
            node = node.next
        return node
    def partition(self,head,tail):
        pivot = tail.val
        i=head
        j=head

        while j != tail:
            if j.val < pivot:
                i.val , j.val = j.val , i.val
                i = i.next
            j = j.next
        i.val , tail.val = tail.val , i.val
        return i
    def quicksorthelper(self,head, tail):
        if head is None or head == tail or head == tail.next :
            return 
        pivot = self.partition(head,tail)
        
        if head != pivot:
            temp = head
            while temp.next != pivot:
                temp = temp.next
            self.quicksorthelper(head,temp)
        if pivot!=tail:
            self.quicksorthelper(pivot.next,tail)

    def quicksort(self):
        if self.head is None:
            return
        tail = self.getTail(self.head)
        self.quicksorthelper(self.head, tail)



x=Solution()
x.insertAtEnd(9)
x.insertAtEnd(2)
x.insertAtEnd(19)
x.insertAtEnd(5)
x.insertAtEnd(18)
x.display()
x.quicksort()
x.display()