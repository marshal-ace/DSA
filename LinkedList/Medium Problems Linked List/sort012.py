# Given the head of a singly linked list consisting of only 0, 1 or 2.
# Sort the given linked list and return the head of the modified list.
# Do it in-place by changing the links between the nodes without creating new nodes.
# Example 1
# Input: linkedList = [1, 0, 2, 0 , 1]
# Output: [0, 0, 1, 1, 2]
# Explanation: The values after sorting are [0, 0, 1, 1, 2].

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None



def create_ll(arr):
    if arr is None:
        return None
    head=Node(arr[0])
    current=head
    for val in arr[1:]:
        value=Node(val)
        current.next=value
        current=current.next
    return head

def optimal(head):
    if head is None or head.next is None:
        return None
    else:
        zeroHead=Node(-1)
        oneHead=Node(-1)
        twoHead=Node(-1)
        zero=zeroHead
        one=oneHead
        two=twoHead
        temp=head
        while temp:
            if temp.val==0:
                zero.next=temp
                zero=zero.next
            elif temp.val==1:
                one.next=temp
                one=one.next
            else:
                two.next=temp
                two=two.next
            temp=temp.next
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
        head=zeroHead.next
        return head