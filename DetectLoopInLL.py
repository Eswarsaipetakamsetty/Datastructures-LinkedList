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

def detectLoop(head:Node):
    slow = head
    fast = head
    while(fast != None and fast.next != None) :
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

arr = [1, 2, 3, 4, 5]
head = convertArrToLL(arr)
head.next.next.next.next.next = head.next.next
print(detectLoop(head))