# 2095. Delete the Middle Node of a Linked List
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.


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
head=create_linked_list([1,3,4,7,1,2,6])

#This is Solved using Tortoise and Hare method where i use one pointer for slow and another pointer for the fast approach so that slow moves one step at a time and the fast pointer moves two steps at a time after the fast pointer reaches the end of the linked list the slow pointer is at the middle  of the linked list i initialized a prev where it remembers the previous node so i can link that to next of middle node so middle is deleted
def delete(head):
    if head is None or head.next is None:
        return None
    else:
        prev=None
        slow=fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head