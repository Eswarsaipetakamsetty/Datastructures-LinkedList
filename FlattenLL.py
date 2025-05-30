class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
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
        print(temp.data)
        print(" | ")
        temp = temp.child
    print()

def merge(l1:Node, l2:Node):
    dummyNode = Node(-1)
    temp = dummyNode
    while(l1 and l2):
        if l1.data < l2.data:
            temp.child = l1
            temp = temp.child
            l1 = l1.child
        else:
            temp.child = l2
            temp = temp.child
            l2 = l2.child
        temp.next = None
    if l1:
        temp.child = l1
    if l2:
        temp.child = l2
    if dummyNode.child: dummyNode.child.next = None
    return dummyNode.child

def flatten(head:Node):
    if head == None or head.next == None:
        return head
    mergedHead = flatten(head.next)
    return merge(head, mergedHead)

arr1 = [1, 2, 4]
arr2 = [4, 5, 6, 8, 9]
head = convertArrToLL(arr1)
head.next.next.child = convertArrToLL(arr2)
head = flatten(head)
printLL(head)
