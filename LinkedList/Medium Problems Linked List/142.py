
# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr, pos):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    nodes = [head]

    for value in arr[1:]:
        node = Node(value)
        current.next = node
        current = current.next
        nodes.append(node)

    if pos != -1:
        current.next = nodes[pos]

    return head


head = create_linked_list([10,20,30,40,50,60], 2)
def check_loop(head):
    if head is None:
        return False
    else:
        hashy={}
        current=head
        while current:
            # val1=hashy.get(current)
            if current in hashy:
                return current
            else:
                # if current.next==None:
                #     return False
                hashy[current]=current.next 
                current=current.next   
        return None


def optimal(head):
    if head is None:
        return None
    else:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                head2=head
                while head2 !=slow:
                    slow=slow.next
                    head2=head2.next
                return head2
        return None