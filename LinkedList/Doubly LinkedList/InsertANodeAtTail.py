class Node:
    def __init__(self,val):
        self.prev=None
        self.val=val
        self.next=None

def create_linked_list(arr):
    if arr is None:
        return None
    head=Node(arr[0])
    current=head
    for value in arr[1:]:
        node=Node(value)
        current.next=node
        node.prev=current
        current=current.next
    return head
head=create_linked_list([4,5,9,1])

def insert_at_tail(head,value):
    if head is None:
        return None
    else:
        current=head
        while current.next is not None:
            current=current.next
        node=Node(value)
        current.next=node
        node.prev=current
    return head
head=insert_at_tail(head,23)
current=head
while current:
    print(current.val,end=" ")
    current=current.next