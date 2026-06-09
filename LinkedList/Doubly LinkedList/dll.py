class Node:
    def __init__(self,val):
        self.prev=None
        self.val=val
        self.next=None

node1=Node(20)
node2=Node(21)
node3=Node(22)
node4=Node(23)



node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3

head=node1
current=head

while current:
    print(current.val,end=" ")
    current=current.next