
# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

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
head=create_linked_list([1,2])

def delete(head,n):
    if head is None:
        return None
    else:
        first=second=head
        i=1
        while i<=n:
            second=second.next
            i+=1
        if second==None:
            return head.next
        prev=None
        while second:
            prev=first
            first=first.next
            second=second.next
        if first.next==None:
            prev.next=None
        else:       
            prev.next=first.next
        return head

            

head2=delete(head,2)
current=head
while current:
    print(current.val)
    current=current.next