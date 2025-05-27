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

def sort012(head:Node):
    if head == None or head.next == None: return head
    zerosH = Node(-1)
    onesH = Node(-1)
    twosH = Node(-1)

    zero = zerosH
    one = onesH
    two = twosH

    temp = head
    while(temp != None):
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next
        temp = temp.next
    zero.next = onesH.next if onesH.next else twosH.next
    one.next = twosH.next
    two.next = None
    return zerosH.next

head = convertArrToLL([0, 2, 0, 1, 2, 0, 2, 0])
printLL(head)
head = sort012(head)
printLL(head)