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

def printDLL(head:Node):
    temp = head
    while(temp):
        print(temp.data, end = " <-> ")
        temp = temp.next
    print()

def deleteAllOccurences(head, key):
    temp = head
    while(temp != None):
        if temp.data == key:
            if temp == head:
                head = head.next
            prev = temp.back
            next = temp.next
            if next:
                next.back = prev
            if prev:
                prev.next = next
            temp = next
        else:
            temp = temp.next
    return head

arr = [1, 1, 1, 4, 6,2, 1, 7, 1]
head = convertArrToDLL(arr)
printDLL(head)
head = deleteAllOccurences(head, 1)
printDLL(head)