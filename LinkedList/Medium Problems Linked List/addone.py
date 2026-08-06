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
            node=Node(ar)
            current.next=node
            current=current.next
    return head
head=create_linked_list([1,9,9])

def add_one(head):
    if head is None:
        return None
    else:
        current=head
        while current:
            if current.val!=9:
                safe=current
            current=current.next
        if safe is None:
            new_head=Node(1)
            new_head.next=head
            current=head
            while current:
                current.val=0
                current=current.next
            return new_head
        safe.val=safe.val+1
        current=safe.next
        while current:
            current.val=0
            current/=current.next
        return head
head=add_one(head)
current=head
while current:
    print(current.val)
    current=current.next


#Solving Using Recursion

def helper(node):
    if node==None:
        return 1
    carry=helper(node.next)
    total=carry+node.val
    node.val=total%10
    return total//10
def add(head):
    carry=helper(head)
    if carry:
        new_node=Node(1)
        new_node.next=head
        head=new_node
    return head
