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

def insertBeforeHead(head:Node, val):
    newHead = Node(val, head, None)
    head.back = newHead

    return newHead

def insertBeforeTail(head:Node, val):
    if head.next == None: return insertBeforeHead(head, val)

    tail = head
    while(tail.next != None):
        tail = tail.next
    
    prevNode = tail.back
    newNode = Node(val, tail, prevNode)
    prevNode.next = newNode
    tail.back = newNode
    return head

def insertBeforeKthEle(head:Node, k, val):
    if k == 1:
        return insertBeforeHead(head, val)
    temp = head
    ctr = 0
    while(head!=None):
        ctr += 1
        if ctr == k:
            break
        temp = temp.next
    prevNode = temp.back
    newNode = Node(val, temp, prevNode)
    prevNode.next = newNode
    temp.back = newNode
    return head

def insertBeforeNode(node:Node, val):
    prev = node.back
    newNode = Node(val, node, prev)
    prev.next = node.back = newNode

def printDLL(head:Node):
    temp = head
    while(temp):
        print(temp.data, end = " <-> ")
        temp = temp.next
    print()

arr = [1, 2, 3, 4, 5]
head = convertArrToDLL(arr)
printDLL(head)
insertBeforeNode(head.next, 10)
printDLL(head)