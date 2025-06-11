from math import floor

class LinkedListNode:
    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next
    
def task(head):
    n = 0
    node = head
    while node:
        n +=1
        node = node.next
    target = floor((2*n/3) - 1)
    if n<2: return None
    cur = 0
    while cur != target:
        head = head.next
        cur += 1
    return head.value
            
head = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5, LinkedListNode(6, LinkedListNode(7))))))))
result = task(head)
print(result)