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

def pairsWithSum(head:Node, s):
    if head == None: return []
    right = head
    while(right.next != None):
        right = right.next
    left = head
    res = []
    while(left.data < right.data):
        if left.data + right.data == s:
            res.append([left.data, right.data])
            left = left.next
            right = right.back
        elif(left.data + right.data < s):
            left = left.next
        else:
            right = right.back
    return res

arr = [1, 2, 3, 4, 5, 6]
head = convertArrToDLL(arr)
printDLL(head)
print(pairsWithSum(head, 5))


    
    