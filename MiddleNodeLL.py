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

def middleNode(head:Node):
    fast = head
    slow = head
    while(fast.next != None and fast != None):
        fast = fast.next.next
        slow = slow.next
    return slow

arr = [1, 2, 4, 5, 6, 7]
head = convertArrToLL(arr)
printLL(head)
middle = middleNode(head)
print(middle.data)