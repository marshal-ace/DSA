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



def reverse(head):
    if head==None:
        return None
    elif head.next==None:
        return head
    else:
        current=head

        while current:
            temp=current.next
            current.next=current.prev
            current.prev=temp
            if temp is None:
                head=current
            current=temp
    return head

head=reverse(head)
current=head
while current:
    print(current.val,end=" ")
    current=current.next