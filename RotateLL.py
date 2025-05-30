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

def findNthNode(temp:Node, k):
    ctr = 1
    while(temp != None):
        if ctr == k:
            return temp
        ctr += 1
        temp = temp.next
    return temp
def rotateLL(head:Node, k):
    length = 1
    tail = head
    while(tail.next != None):
        tail = tail.next
        length += 1
    if(k%length == 0): return head
    tail.next = head
    k = k % length
    newLastNode = findNthNode(head, length - k)
    head = newLastNode.next
    newLastNode.next = None
    return head

arr = [10, 20, 30, 40, 50]
head = convertArrToLL(arr)
printLL(head)
head = rotateLL(head, 4)
printLL(head)