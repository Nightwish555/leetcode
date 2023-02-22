# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for sub_list in lists:
            while sub_list:
                heap.append(sub_list.val)
                sub_list = sub_list.next
        heap.sort(reverse=True)

        head = ListNode(None)
        curr_list = head
        while heap:
            # 从heap列表的尾部取最小数加入到链表中
            temp_list = ListNode(heap.pop())
            curr_list.next = temp_list
            curr_list = curr_list.next
        return head.next
