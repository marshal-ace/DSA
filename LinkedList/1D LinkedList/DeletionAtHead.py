#We are given a Linked List we need to Delete the head of the Linkedlist and return it

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

head=created_linked_list([22,23,24,25,26,27])

def deletion_head(head):
    if head is None:
        return None
    else:
        temp=head.next
        head=temp
    return head
new_head=deletion_head(head)
print(new_head.data)