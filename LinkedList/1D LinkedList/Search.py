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

head=create_linked_list([22,21,23,24,25,26,27])

def search_linked_list(head,value):
    if head is None:
        return None
    else:
        current=head
        while current is not None:
            if current.data == value:
                return True
            current=current.next
    return False
            

print(search_linked_list(head,27))
