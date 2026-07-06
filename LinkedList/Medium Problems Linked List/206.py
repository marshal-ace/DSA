
# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Node:
    def __init__(self,val):
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
        current=current.next
    return head
head=create_linked_list([1,2,3])

def reverse_a_ll(head):
    if head is None:
        return None
    elif head.next==None:
        return head
    else:
        prev=None
        next2=head.next
        current=head
        while current:
            next2=current.next
            current.next=prev
            prev=current
            current=next2
    return prev
ans=reverse_a_ll(head)
current=ans
while current:
    print(current.val)
    current=current.next