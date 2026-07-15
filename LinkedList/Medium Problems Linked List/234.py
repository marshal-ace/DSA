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
head=create_linked_list([1,2,2,1])
#TC O(N)--SC O(N)
def check_palindrome(head):
    if head is None:
        return None
    else:
        check=[]
        current=head
        while current:
            check.append(current.val)
            current=current.next
        # print(check)
        rev=list(reversed(check))
        # print(rev)
        if check == rev:
            return True
        else:
            return False
print(check_palindrome(head))
#Here we use two concepts reverse a linked list and finding the middle of linked list

#TC-O(N),SC-O(1)
def optimal(head):
    if head is None:
        return None
    else:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        middle = slow
        prev=next2=None
        while middle:
            next2=middle.next
            middle.next=prev
            prev=middle
            middle=next2
        # slow.next=None
        current=head
        while current and prev:
            if current.val!=prev.val:
                return False
            current=current.next
            prev=prev.next
        return True
print(optimal(head))