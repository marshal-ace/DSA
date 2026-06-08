# Problem: Insert a Node at a Given Position in a Singly Linked List
# Given the head of a singly linked list, an integer value, and a zero-based integer position, insert a new node with the given value at the specified position.
# If position = 0, insert the node at the beginning of the list.
# It is guaranteed that 0 ≤ position ≤ length of the linked list.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

def created_linked_list(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current=head

    for value in arr[1:]:
        current.next=Node(value)
        current=current.next
    return head
head=created_linked_list([4,5,9,1])

def insert(head,value,position):
    node=Node(value)
    if position==0:
        node.next=head
        head=node
    else:
        count=0
        current=head
        prev=None
        while current is not None:
            if position==count:
                node.next=prev.next
                prev.next=node
                break
            prev=current
            current=current.next
            count+=1
    if current is None and count == position:
        prev.next=node
    return head
# ----------------------------
#Cleanest Way to insert'
#Here we stop before the position we need to insert and do the insertion
def insert2(head,value,position):
    node = Node(value)
    if position==0:
        node.next=head
        return node
    count=0
    current=head
    while count<position-1:
        current=current.next
        count+=1
    node.next=current.next
    current.next=node
    return head


# head=insert(head,23,4)
head=insert2(head,23,4)
current=head

while current is not None:
    print(current.data,end=" ")
    # print(current.next)
    current=current.next



