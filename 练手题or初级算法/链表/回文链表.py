# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pre = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != pre.val:
                return False
            pre = pre.next
            slow = slow.next
        return True