#Inserting the Node at the end of the LinkedList

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def create_linked_list(arr):
    if arr is None:
        return None
    head=Node(arr[0])
    current=head
    for val in arr[1:]:
        current.next=Node(val)
        current=current.next
    return head
head=create_linked_list([4,5,9,1])

def insert_at_tail(head,valee):
    node=Node(valee)
    if head is None:
        return node
    else:
        current=head
        while current is not None:
            if current.next==None:
                current.next=node
                break
            current=current.next
    return head
head=insert_at_tail(head,23)
current=head

while current is not None:
    print(current.val,end=" ")
    # print(current.next)
    current=current.next
