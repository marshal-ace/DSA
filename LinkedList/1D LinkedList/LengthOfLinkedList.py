class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_linked_list(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current=head

    for value in arr[1:]:
        current.next=Node(value)
        current=current.next
    return head
head=create_linked_list([])

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