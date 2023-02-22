# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2) -> Optional[ListNode]:
        l1.val += l2.val
        if l1.val > 10:
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
            l1.val %= 10
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1
