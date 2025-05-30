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


def startingPointOfLoop(head:Node):
    fast = head
    slow = head
    while(fast.next != None and fast.next.next != None):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = head
            while(slow != fast):
                slow = slow.next
                fast = fast.next
            return slow
    return None

arr = [1, 2, 3, 4, 5]
head = convertArrToLL(arr)
head.next.next.next.next.next = head.next
print(startingPointOfLoop(head).data)
