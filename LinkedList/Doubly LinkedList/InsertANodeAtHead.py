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

def insertion_at_head(head,data):
    node=Node(data)
    if head is None:
        return node
    else:
        head.prev=node
        node.next=head
        head=node
    return head

new_head=insertion_at_head(head,23)
current=new_head
while current:
    print(current.val,end=" ")
    current=current.next
