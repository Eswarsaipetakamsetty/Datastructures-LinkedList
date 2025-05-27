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

def removeHead(head:Node) -> Node:
    if head == None: return head
    head = head.next
    return head

def removeTail(head:Node):
    if head == None or head.next == None: return None
    temp = head
    while(temp.next.next != None):
        temp = temp.next
    temp.next = None
    return head

def removeK(head:Node, k):
    if head == None: return head
    if k == 1:
        head = head.next
        return head
    
    ctr = 0
    temp = head
    prev = None
    while(temp != None):
        ctr += 1
        if ctr == k:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head

def removeEle(head:Node, ele):
    if head == None: return head
    if head.data == ele:
        head = head.next
        return head

    temp = head
    prev = None
    while(temp != None):
        if temp.data == ele:
            prev.next = prev.next.next
            break
        prev = temp
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
head = removeEle(head, 1)
printLL(head)
