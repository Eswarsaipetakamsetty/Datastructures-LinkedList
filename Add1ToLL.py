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

def add1ToLL(head:Node):
    if head == None:
        return head
    
    if head.next == None:
        s = head.data + 1
        carry = s%10
        if s>9:
            head.data = s//10
            newNode = Node(s%10)
            head.next = newNode
            return head
        else:
            head.data = s
            return head
    
    newHead = Reverse(head)
    temp = newHead
    carry = 1
    while(temp!= None):
        temp.data = temp.data + carry
        if temp.data < 10:
            carry = 0
            break
        else:
            temp.data = 0
            carry = 1
        temp = temp.next
    if carry == 1:
        newNode = Node(carry)
        head = Reverse(newHead)
        newNode.next = head
        return newNode
    
    head = Reverse(newHead)
    return head

#optmial
def helper(temp:Node):
    if temp == None:
        return 1
    carry = helper(temp.next)
    temp.data = temp.data + carry
    if temp.data < 10:
        return 0
    temp.data = 0
    return 1


def add1ToLLRec(head:Node):
    carry = helper(head)
    if carry == 1:
        newNode = Node(1)
        newNode.next = head
        return newNode
    return head

arr = [9]
head = convertArrToLL(arr)
printLL(head)
head = add1ToLLRec(head)
printLL(head)
    
