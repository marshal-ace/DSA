
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
 #  A: 4 -> 1-----\
 #                 8 -> 4 -> 5
# B: 5 -> 6 -> 1 /

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


# Common part (intersection)
common = create_linked_list([8, 4, 5])

# List A: 4 -> 1 -> 8 -> 4 -> 5
headA = create_linked_list([4, 1])
temp = headA
while temp.next:
    temp = temp.next
temp.next = common

# List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
headB = create_linked_list([5, 6, 1])
temp = headB
while temp.next:
    temp = temp.next
temp.next = common

def intersection(headA,headB):
    if headA is None and headB is None:
        return None
    else:
        current=headA
        len_A=len_B=diff=0
        while current:
            len_A+=1
            current=current.next
        current=headB

        while current:
            len_B+=1
            current=current.next
        A_pointer=headA
        B_pointer=headB
        if len_A>len_B:
            diff=len_A-len_B
            i=0
            while i<diff:
                A_pointer=A_pointer.next
                i+=1
        else:
            diff=len_B-len_A
            i=0
            while i<diff:
                B_pointer=B_pointer.next
                i+=1
        while A_pointer and B_pointer:
            if A_pointer==B_pointer:
                return A_pointer
            A_pointer=A_pointer.next
            B_pointer=B_pointer.next
        return None
