class Node:
    def __init__(self,val):
        self.prev=None
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
        node.prev=current
        current=current.next
    return head
    
head=create_linked_list([4,5,9,1])

def Length_of_ll(head):
    if head is None:
        return 0
    else:
        count=0
        current=head
        while current is not None:
            count+=1
            current=current.next
    return count
count=Length_of_ll(head)
print(count)