# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    seen = {0: dummy}

    while head:
        prefix_sum += head.val

        if prefix_sum in seen:
            prev = seen[prefix_sum]
            temp = prev.next
            sum_to_remove = prefix_sum
            while temp != head:
                sum_to_remove += temp.val
                del seen[sum_to_remove]
                temp = temp.next
            prev.next = head.next
        else:
            seen[prefix_sum] = head

        head = head.next

    return dummy.next
