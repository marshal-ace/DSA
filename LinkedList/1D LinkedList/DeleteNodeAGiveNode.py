class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

def created_linked_list(arr):
    if not arr:
        return None
    head=Node(arr[0])
    current=head

    for value in arr[1:]:
        current.next=Node(value)
        current=current.next
    return head

def delete_node(head,value):
    if head is None:
        return None
    else:
        current=head
        while current is not None:
            if head.data==value:
                temp=head.next
                head=temp
                current=head
                break
            #This is used to check if the next node exists
            elif current.next !=None:
                if current.next.data==value:
                    if current.next.next==None:
                        current.next=None
                    else:
                        current.next=current.next.next
            current=current.next
    return head

#This is my using Prev where we store the previous node by using this there is no need to handle the case of last node
def delete_node_prev(head,value):
    if head is None:
        return None
    else:
        current=head
        prev=None
        while current is not None:
            if head.data==value:
                temp=head.next
                head=temp
                current=head
                break
            elif current.data==value:
                prev.next=current.next
                break
            prev=current
            current=current.next