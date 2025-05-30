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

def deleteMiddleNode(head:Node):
    fast = head
    slow = head
    prev = None
    while(fast != None and fast.next != None):
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = prev.next.next


arr = [1, 2, 3, 4, 4, 5]
head = convertArrToLL(arr)
deleteMiddleNode(head)
printLL(head)