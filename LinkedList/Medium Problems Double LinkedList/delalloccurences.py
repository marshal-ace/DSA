# Given the head of a doubly linked list and an integer target. Delete all nodes in the linked list with the value target and return the head of the modified linked list.

# Input: head -> 1 <-> 2 <-> 3 <-> 1 <-> 4, target = 1
# Output: head -> 2 <-> 3 <-> 4
# Explanation: All nodes with the value 1 were removed.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def array_to_dll(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])

        current.next = new_node
        new_node.prev = current

        current = new_node

    return head

head=array_to_dll([1,2,3,1,4])


def del_all(head,target):
    current=head
    if head is None:
        return None
    else:
        if head==target and head.next==None:
             return None
        while current:
            if current.data==target and current==head:
                current.next.prev=None
                head=current.next
            elif current.data==target and current.next==None:
                        current.prev.next=None
            elif current.data==target:
                current.next.prev=current.prev
                current.prev.next=current.next
            current=current.next
        return head
head=del_all(head,1)

current=head
while current:
    print(current.data)
    current=current.next
    