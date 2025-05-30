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

def collisionPoint(head1:Node, head2:Node, d):
    first = head1
    second = head2
    for i in range(d):
        second = second.next
    
    while(first != second):
        first = first.next
        second = second.next
    return first


def intersectionNodeOfYLL(head1:Node, head2:Node):
    t1 = head1
    l1 = 0
    t2 = head2
    l2 = 0
    while(t1 != None or t2 != None):
        if t1 != None:
            l1 +=1
            t1 = t1.next
        if t2 != None:
            l2 += 1
            t2 = t2.next
    if l1 < l2:
        return collisionPoint(head1, head2, l2 - l1)
    else:
        return collisionPoint(head2, head1, l1 - l2)
    

def intersectionOfLL(head1:Node, head2:Node):   #optimal
    if head1 == None or head2 == None:
        return None
    t1 = head1
    t2 = head2
    while(t1 != t2):
        t1 = t1.next
        t2 = t2.next

        if t1 == t2:
            return t1

        if t1 == None:
            t1 = head2
        if t2 == None:
            t2 = head1
    return t1

arr1 = [1, 2, 3]
arr2 = [1, 2, 2, 3]
head1 = convertArrToLL(arr1)
head2 = convertArrToLL(arr2)
arr3 = [1, 2, 4, 6, 4]
tail = convertArrToLL(arr3)
head1.next.next.next = tail
head2.next.next.next.next = tail
printLL(head1)
printLL(head2)
res = intersectionOfLL(head1, head2)
printLL(res)


