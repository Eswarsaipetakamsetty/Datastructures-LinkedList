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

def removeDuplicates(head:Node):
    if head == None:
        return
    temp = head
    while(temp.next != None):
        if temp.data == temp.next.data:
            if temp.next.next != None:
                temp.next = temp.next.next
                temp.next.back = temp
            else:
                dup = temp.next
                temp.next = None
                dup.back = None
        else:
            temp = temp.next

arr = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5]
head = convertArrToDLL(arr)
printDLL(head)
removeDuplicates(head)
printDLL(head)