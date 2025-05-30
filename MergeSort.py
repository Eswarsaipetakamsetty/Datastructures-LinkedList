class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

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

def merge(h1:Node, h2:Node):
    if not h1 or not h2:
        return h1 if h1 else h2
    l1 = h1
    l2 = h2
    dummyNode = Node(-1)
    res = dummyNode
    while(l1 != None and l2 != None):
        if l1.data < l2.data:
            res.next = l1
            res = res.next 
            l1 = l1.next
        else:
            res.next = l2
            res = res.next
            l2 = l2.next 
    if l1:
        res.next = l1
    if l2:
        res.next = l2
    return dummyNode.next

def getMiddle(head:Node):
    fast = head.next
    slow = head
    while(fast != None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
    return slow

def mergeSort(head:Node):
    if head == None or head.next == None : return head
    middle = getMiddle(head)
    leftHead = head
    rightHead = middle.next
    middle.next = None
    leftHead = mergeSort(leftHead)
    rightHead = mergeSort(rightHead)
    return merge(leftHead, rightHead)

arr = [1, 5, 2, 65, 3, 6,2, 6, 3, 5, 1, 4, 55]
head = convertArrToLL(arr)
head = mergeSort(head)
printLL(head)