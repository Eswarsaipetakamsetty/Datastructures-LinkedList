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

def Reverse(head:Node): #iterative
    if head == None or head.next == None: return head
    temp = head
    prev = None
    while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def ReverseRec(head:Node): #recursive
    if head == None or head.next == None:
        return head
    newHead = ReverseRec(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newHead


arr = [1, 2, 3, 4, 5]
head = convertArrToLL(arr)
head = Reverse(head)
printLL(head)
head = ReverseRec(head)
printLL(head)
    