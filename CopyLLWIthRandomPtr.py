class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None
    

def convertArrToLL(arr:list) -> Node:
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

def printLL(head:Node):
    temp = head
    while(temp):
        print(temp.data, end = " -> ")
        temp = temp.next
    print()

def copyListWithRandomPtr(head:Node):
    temp = head
    while temp != None:
        newNode = Node(temp.data)
        newNode.next = temp.next
        temp.next = newNode
        temp = temp.next.next
    temp = head
    while temp != None:
        if temp.random:
            temp.next.random = temp.random.next 
        else:
            temp.next.random = None
        temp = temp.next.next 
    dummyNode = Node(-1)
    res = dummyNode
    temp = head
    while temp != None:
        res.next = temp.next
        temp.next = temp.next.next
        res = res.next
        temp = temp.next
    return dummyNode.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.random = None
head.next.random = head.next.next.next
head.next.next.random = head
ans = copyListWithRandomPtr(head)
printLL(ans)