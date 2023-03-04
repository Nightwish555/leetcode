# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 	def reverse(pre,cur):
    #         if cur is None:
    #             return pre
    #         temp = cur.next
    #         cur.next = pre #转向

    #         #进入下一层递归/同下一个while循环
    #         return reverse(cur,temp)
    #     return reverse(None,head)
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(pre, cur):
            if cur is None:
                return pre

            tmp = cur.next
            cur.next = pre  # 转向
            # 进入下一层递归
            return reverse(cur, tmp)

        return reverse(None, head)