# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

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
l1=create_linked_list([1,2])
l2=create_linked_list([1,2,3,4,5])

def mergeTwoLists(l1,l2):
        if not list1:
            return list2
        if not list2:
            return list1
        else:
            dummyNode=Node(-1)
            dummy=dummyNode
            while list1 and list2:
                if list1.val<list2.val:
                    dummy.next=list1
                    list1=list1.next
                else:
                    dummy.next=list2
                    list2=list2.next
                dummy=dummy.next
            if list1:
                dummy.next=list1
            else:
                dummy.next=list2
        return dummyNode.next

