# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

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
head=create_linked_list([20,21,22,23,24,25])
def length(head):
    if head is None:
        return None
    else:
        current=head
        count=0
        while current:
            current=current.next
            count+=1
    #This returns the position
    return (count//2)+1
count=length(head)
# print(count)
def two_pass(head,count):
    #Here at first loop we get the Length of LinkedList and return it (length//2)+1 from here we get position
    #In the second pass we find the middle node and return it
    current=head
    i=1

    while i<count:
        # print(f"{i}  {current.val}")
        current=current.next
        i+=1
    return current
# print(current.val)

def onepass(head):
    #This is the tortoise and hare method where slow and fast pointers are used
    slow=fast=current=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow

print(onepass(head).val)