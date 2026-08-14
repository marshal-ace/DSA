# Find Pairs with Given Sum in Doubly Linked List
# Given the head of a sorted doubly linked list of positive distinct integers, and a target integer, return a 2D array containing all unique pairs of nodes (a, b) such that a + b == target.
# Each pair should be returned as a 2-element array [a, b] with a < b. The list is sorted in ascending order. If there are no such pairs, return an empty list.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def array_to_dll(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])

        current.next = new_node
        new_node.prev = current

        current = new_node

    return head

head=array_to_dll([1,2,4,5,6,8,9])

def find_pairs(head,target):
    if head is None:
        return None
    else:
        list=[]
        current=head
        hashy={}
        while current:
            if target-current.data in hashy:
                list.append([target-current.data,current.data])
            else:
                hashy[current.data]=current
            current=current.next
        return list
# print(find_pairs(head,7))


def optimal(head,target):
    if head is None:
        return None
    else:
        ans=[]
        small=large=head
        while large.next:
            large=large.next
        while large.data>=small.data:
            sum=large.data+small.data
            if sum>target:
                large=large.prev
            elif sum<target:
                small=small.next
            elif sum==target:
                ans.append([small.data,large.data])
                small=small.next
                large=large.prev
        return ans
print(optimal(head,7))

