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

def reverse(temp:Node):
    prev = None
    while(temp != None):
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

def getKthNode(temp:Node, k):
    k -= 1
    while(temp != None and k > 0):
        k -= 1
        temp = temp.next
    return temp
def reverseNodesInKGroup(head:Node, k):
    prevNode = None
    temp = head
    while(temp != None):
        kThNode = getKthNode(temp, k)
        if(kThNode == None):
            if prevNode != None:
                prevNode.next = temp
            break
        nextNode = kThNode.next
        kThNode.next = None
        reverse(temp)
        if(temp == head):
            head = kThNode
        else:
            prevNode.next = kThNode
        prevNode = temp
        temp = nextNode
    return head

arr = [1, 2, 3, 4, 5, 6, 7, 8]
head = convertArrToLL(arr)
printLL(head)
head = reverseNodesInKGroup(head, 3)
printLL(head) 

