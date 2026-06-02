#Given the head of a singly linked list and an integer X, insert a node with value X at the head of the linked list and return the head of the modified list.
# Example 1

# Input: linkedList = [1, 2, 3], X = 7

# Output: [7, 1, 2, 3]

# Explanation:

# 7 was added as the 1st node.


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def create_linked_list(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current=head

    for value in arr[1:]:
        current.next=Node(value)
        current=current.next
    return head
head = create_linked_list([])    

def head_change(head,value):
    if head is None:
        head=Node(value)
    else:
        current=Node(value)
        current.next=head
        head=current
    return head
new_head=head_change(head,23)
print(new_head.data)

    