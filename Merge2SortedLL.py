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

def merge(head1:Node, head2:Node):
    if not head1 or not head2:
        return head1 if head1 else head2
    l1 = head1
    l2 = head2
    dummyNode = Node(-1)
    temp = dummyNode
    while(l1 != None and l2 != None):
        if(l1.data < l2.data):
            temp.next = l1
            temp = temp.next
            l1 = l1.next
        else:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
    
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return dummyNode.next

arr1 = [1, 2, 4, 5, 7]
arr2 = [3, 6, 7, 8, 28, 77]
head1 = convertArrToLL(arr1)
head2 = convertArrToLL(arr2)
head = merge(head1, head2)
printLL(head)
