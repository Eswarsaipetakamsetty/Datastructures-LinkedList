class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Solution(Node):
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def display(self):
        temp=self.head
        while temp:
            print(temp.value,"->",end="")
            temp=temp.next
x=Solution()
x.insert(1)
x.insert(2)
x.insert(3)
x.display()
