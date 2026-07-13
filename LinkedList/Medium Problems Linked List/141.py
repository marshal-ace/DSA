# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

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


head = create_linked_list([1,2], -1)

#Better Approach 
#SC-0(n) #TC-0(n)
def check_loop(head):
    if head is None:
        return False
    else:
        hashy={}
        current=head
        while current:
            # val1=hashy.get(current)
            if current in hashy:
                return True
            else:
                # if current.next==None:
                #     return False
                hashy[current]=current.val
                current=current.next   
        return False
print(check_loop(head))     

#Using The Tortoise and Hare method
#Basically One is a slow pointer and other is a fast pointer slow pointer moves
# one node at a time and the fast pointer moves two at a time eventually the slow and fast catches up to the slow pointer 
# when the fast == slow it means there is a loop this is the optimized way like O(1) for the Space
#TC-O(N), SC-O(1)
def check_optimize(head):
    if head is None:
        return None
    else:
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
print(check_optimize(head))