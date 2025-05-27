class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def convertArrToLL(arr:list) -> Node:
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

def insertHead(head:Node, val):
    temp = Node(val)
    temp.next = head
    return temp

def insertTail(head:Node, val):
    if head == None:
        return Node(val)
    temp = head
    while(temp.next != None):
        temp = temp.next
    temp.next = Node(val)
    return head

def insertK(head:Node, val, k):
    if head == None:
        if k == 1:
            return Node(val)
        return head
    if k == 1:
        newNode = Node(val)
        newNode.next = head
        return newNode
    ctr = 0
    temp = head
    while(temp != None):
        ctr += 1
        if ctr == k - 1:
            newNode = Node(val)
            newNode.next = temp.next
            temp.next = newNode
            break
        temp = temp.next
    return head

def insertBeforeValue(head:Node, val, ele):
    if head == None:
        return head
    if head.data == val:
        newNode = Node(ele)
        newNode.next = head
        return newNode
    temp = head
    while(temp != None):
        if temp.next.data == val:
            newNode = Node(ele)
            newNode.next = temp.next
            temp.next = newNode
            break
        temp = temp.next
    return head

def printLL(head:Node):
    temp = head
    while(temp):
        print(temp.data, end = " -> ")
        temp = temp.next
    print()

arr = [1, 3, 4, 6, 7]
head = convertArrToLL(arr)
printLL(head)
head = insertBeforeValue(head, 7, 5)
printLL(head)