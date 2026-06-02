class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(20)
node2=Node(21)
node3=Node(22)
node4=Node(23)

node1.next=node2
node2.next=node3
node3.next=node4

current=node1

while current is not None:
    print(current.data,end="->")
    print(current.next)
    current=current.next
print("None")