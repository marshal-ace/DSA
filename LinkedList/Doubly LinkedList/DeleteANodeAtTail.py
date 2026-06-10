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

def delete_tail(head):
    if head is None or head.next==None:
        return None
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.prev.next=None
        return head
    
head=delete_tail(head)
current=head
while current:
    print(current.val,end=" ")
    current=current.next