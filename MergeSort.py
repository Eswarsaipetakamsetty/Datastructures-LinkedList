class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = None
class LinkedList(Node):
    def __init__(self):
        self.head = None
    def insert(self,data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.head = Node(data)
    def printList(self , head):
        temp = head
        while temp:
            print(temp.val, end = "-->")
            temp = temp.next
        print(None)
    def getTail(head):
        temp = head
        while temp.next:
            temp = temp.next
        return temp
    def merge(l1 , l2):
        pass