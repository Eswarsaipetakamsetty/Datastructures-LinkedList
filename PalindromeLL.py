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

def Reverse(head: Node):
    if head == None or head.next == None:
        return head
    temp = head
    prev = None
    while(temp != None):
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def middleNode(head:Node):
    fast = head
    slow = head
    while(fast.next != None and fast.next.next != None):
        fast = fast.next.next
        slow = slow.next
    return slow

def palindrome(head:Node):
    if head == None or head.next == None: return True
    middle = middleNode(head)
    newHead = Reverse(middle.next)
    first = head
    second = newHead
    while second != None:
        if first.data != second.data:
            Reverse(newHead)
            return False
        first = first.next
        second = second.next
    Reverse(newHead)
    return True

arr = [1, 2, 3, 2, 1]
head = convertArrToLL(arr)
printLL(head)
print(palindrome(head))



