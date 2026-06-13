#This is a double linked list a node is given and we have to delete that node

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


def delete_a_node(head,value):
    if head is None or head.next==None:
        return None
    elif head.val==value:
        head=head.next
        head.prev=None
    else:
        current=head
        while current.val!=value:
            current=current.next
            if current is None:
                return None
        if current.next==None:
            current.prev.next=None
        else:
            current.next.prev=current.prev
            current.prev.next=current.next
    return head

head=delete_a_node(head,100)

current=head
while current:
    print(current.val,end=" ")
    current=current.next