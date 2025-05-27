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
        
    
def checkIfPresent(head:Node, key):
    temp = head
    while(temp):
        if temp.data == key:
            return True
        temp = temp.next
    return False

arr = [1, 2, 3, 4, 5]
head = convertArrToLL(arr)
print(checkIfPresent(head, 3))

