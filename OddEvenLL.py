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

def OddEvenList(head:Node):
    if head == None or head.next == None: return head
    odd = head
    evenHead = head.next
    even = head.next
    while(even != None and even.next != None):
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    
    odd.next = evenHead
    return head

arr = [1, 2, 3, 4 ,5, 6]
head = convertArrToLL(arr)
printLL(head)
head = OddEvenList(head)
printLL(head)