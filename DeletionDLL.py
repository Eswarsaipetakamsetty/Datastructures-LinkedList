class Node:
    def __init__(self, data1, next1 = None, back1 = None):
        self.data = data1
        self.next = next1
        self.back = back1

def convertArrToDLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head

def removeHead(head:Node):
    if head == None or head.next == None: return None
    prev = head
    head = head.next
    head.back = None
    prev.next = None
    return head

def removeTail(head:Node):
    if head == None or head.next == None: return None
    tail = head
    while(tail.next != None):
        tail = tail.next
    newtail = tail.back
    newtail.next = None
    tail.back = None
    return head

def removeKthEle(head:Node, k):
    if head == None: return None
    kNode = head
    ctr = 0
    while(kNode != None):
        ctr += 1
        if ctr == k:
            break
        kNode = kNode.next
    prevNode = kNode.back
    nextNode = kNode.next

    if(prevNode == None and nextNode == None):
        return None
    elif (prevNode == None):
        return removeHead(head)
    elif (nextNode == None):
        return removeTail(head)
    
    prevNode.next = nextNode
    nextNode.back = prevNode
    kNode.next = None
    kNode.back = None
    return head

def removeNode(temp:Node):
    prevNode = temp.back
    nextNode = temp.next

    if nextNode == None:
        prevNode.next = None
        temp.back = None
        return
    prevNode.next = nextNode
    nextNode.back = prevNode
    temp.next = temp.back = None

def printDLL(head:Node):
    temp = head
    while(temp):
        print(temp.data, end = " <-> ")
        temp = temp.next
    print(None)


arr = [1, 2, 3, 4, 5]
head = convertArrToDLL(arr)
removeNode(head.next)
printDLL(head)
