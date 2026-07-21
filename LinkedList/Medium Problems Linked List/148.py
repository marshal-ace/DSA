# 148. Sort List
# Given the head of a linked list, return the list after sorting it in ascending order.


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
        for ar in arr[1:]:
            value=Node(ar)
            current.next=value
            current=current.next
    return head
#Brute force solution TC-O(n log n) SC-O(N)
#Here copy every value of linked list into an array and sort the array and while traversing the LL replace the values 
def sort_ll(head):
    if head is None:
        return None
    else:
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        arr=sorted(arr)
        print(arr)
        i=0
        current=head
        while current:
            current.val=arr[i]
            # print(i)
            i+=1
            current=current.next
        return head

head=create_linked_list([1,5,7,23,11])
head=sort_ll(head)

current=head
while current:
    print(current.val)
    current=current.next