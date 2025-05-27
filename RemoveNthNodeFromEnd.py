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

def RemoveNthNodeFromEnd(head:Node, n):
    fast = head
    slow = head
    for i in range(n):
        if fast.next == None:
            return head
        fast = fast.next
    if fast == None:
        return head.next
    while(fast.next != None):
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

head = convertArrToLL([1, 2, 3, 5, 6, 7])
head = RemoveNthNodeFromEnd(head, 3)
printLL(head)
