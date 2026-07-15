# Given the head of a singly linked list, find the length of the loop in the linked list if it exists. Return the length of the loop if it exists; otherwise, return 0.
# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos is used to denote the index (0-based) of the node from where the loop starts.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr, pos):
    if not arr:
        return None
    head = Node(arr[0])
    current = head

    nodes = [head]

    for value in arr[1:]:
        node = Node(value)
        current.next = node
        current = current.next
        nodes.append(node)

    if pos != -1:
        current.next = nodes[pos]

    return head

#This uses Floyd Algo(Tortoise and Hare) using Slow and fast pointer
# First we need to detect the loop and take one of the pointer and loop until it meets the other point and along the way it counts the loop 
# if there is no loop return 0
head = create_linked_list([10,20,30,40,50,60], 2)
def check_loop(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            count=1
            temp=slow.next
            while temp!=slow:
                count+=1
                temp=temp.next
            return count
    return 0
print(check_loop(head))