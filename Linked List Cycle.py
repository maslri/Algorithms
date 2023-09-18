
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Linked_list:
    def __init__(self, ListNode):
        self.head = ListNode
    
    def hasCycle(self) -> bool:
        slow = fast = self.head
        while slow and fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        else :
            return False

    def __str__(self):
        _str = ""
        temp = self.head
        while temp.next:
            _str += str(temp.data) + " --> "
            temp = temp.next
        else:
            _str += str(temp.data)
        return _str
    
class Solution:
    def hasCycle(self, head: Linked_list[ListNode]) -> bool:
        self.hasCycle(head)