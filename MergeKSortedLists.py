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

def merge2LL(head1:Node, head2:Node):
    if not head1 or not head2:
        return head1 if head1 else head2
    
    l1 = head1
    l2 = head2
    dummyNode = Node(-1)
    res = dummyNode
    while(l1 != None and l2 != None):
        if l1.data < l2.data:
            res.next = l1
            res = res.next
            l1 = l1.next
        else:
            res.next = l2
            res = res.next
            l2 = l2.next
    if l1:
        res.next = l1
    if l2:
        res.next = l2
    return dummyNode.next

def mergeK(l:list[Node]):
    head = l[0]
    for i in range(1, len(l)):
        head = merge2LL(head, l[i])
    return head


#optimal
from queue import PriorityQueue
from itertools import count
def mergeKSorted(l:list[Node]):
    counter = count()
    pq = PriorityQueue()
    for i in range(len(l)):
        pq.put((l[i].data, next(counter), l[i]))
    dummyNode = Node(-1)
    res = dummyNode
    while(not pq.empty()):
        _, _, node = pq.get()
        res.next = node
        if node.next:
            pq.put((node.next.data, next(counter), node.next))
        res = res.next
    return dummyNode.next

arr1 = [1, 2, 3, 5]
arr2 = [1, 3, 5, 7]
arr3 = [1, 8, 10]
head1 = convertArrToLL(arr1)
head2 = convertArrToLL(arr2)
head3 = convertArrToLL(arr3)
arr = [head1, head2, head3]
head = mergeKSorted(arr)
printLL(head)
