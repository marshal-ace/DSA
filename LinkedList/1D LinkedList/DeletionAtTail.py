#To Delete the node at the end 
class Node:
    def __init__(self,val):
        self.val=val
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
def deletion(head):
    if head is None or head.next==None:
        return None
    else:
        current=head
        prev=None
        while current is not None:
            if current.next==None:
                prev.next=None
                break
            prev=current
            current=current.next
    return head
head=deletion(head)
current=head
while current is not None:
    print(current.val,end=" ")
    # print(current.next)
    current=current.next
# --------------------------------
#Another way to Delete the Last Node
def deletion2(head):
    if head is None or head.next==None:
        return None
    else:
        while current.next.next is not None:
            current=current.next
        current.next=None
    return head