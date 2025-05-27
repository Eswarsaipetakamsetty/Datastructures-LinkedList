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


def addLL(l1:Node, l2:Node):
    dummyNode = Node(-1)
    curr = dummyNode
    t1 = l1
    t2 = l2
    carry = 0
    while(t1 != None or t2 != None):
        s = carry
        if t1: s += t1.data
        if t2: s += t2.data

        newNode = Node(s%10)
        carry = s//10

        curr.next = newNode
        curr = curr.next

        if t1: t1 = t1.next
        if t2: t2 = t2.next
    
    if carry:
        newNode = Node(carry)
        curr.next = newNode
    return dummyNode.next

head1 = convertArrToLL([3, 5])
head2 = convertArrToLL([4, 5, 9, 9])

res = addLL(head1, head2)
printLL(res)

