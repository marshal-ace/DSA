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


def insert(head,position,value):
    if head is None:
        return None
    elif position==0:
        node=Node(value)
        head.prev=node
        node.next=head
        head=node
    else:
        node=Node(value)
        current=head
        count=0
        while count<position-1:
            current=current.next
            count+=1
        if current.next==None:
            node.prev=current
            current.next=node
        else:
            node.next = current.next
            node.prev = current

            current.next.prev = node
            current.next = node

    return head

new_head=insert(head,4,23)
current=new_head
while current:
    print(current.val,end=" ")
    current=current.next