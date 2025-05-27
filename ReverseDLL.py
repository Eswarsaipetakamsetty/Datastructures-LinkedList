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

def Reverse(head:Node):
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    while(curr != None):
        prev = curr.back
        curr.back = curr.next
        curr.next = prev

        curr = curr.back
    return prev.back

def printDLL(head:Node):
    temp = head
    while(temp):
        print(temp.data, end = " <-> ")
        temp = temp.next
    print()


arr = [1, 2, 3, 4, 5]
head = convertArrToDLL(arr)
printDLL(head)
head = Reverse(head)
printDLL(head)