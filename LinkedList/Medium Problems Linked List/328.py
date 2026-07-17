# 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


def create_linked_list(arr):
    if arr is None:
        return None
    else:
        head=Node(arr[0])
        current=head
        for val in arr[1:]:
            node=Node(val)
            current.next=node
            current=current.next
    return head

head=create_linked_list([1,2,3,4,5])

def convert(head):
    if head is None:
        return None
    elif head.next is None:
        return None
    else:
        odd=head
        even=even_head=head.next
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head
        # odd=current=head
        # even=head.next
        # while current and current.next:
        #     current=current.next.next
        #     odd.next=current
        #     odd=odd.next
        # while even and even.next:
        #     odd.next=even
        #     even=even.next.next
        # return odd

head2=convert(head)
current=head2
while current:
    print(current.val)
    current=current.next
