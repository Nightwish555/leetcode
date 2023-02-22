class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        length = 0
        for i in list(s):
            if i in queue:
                length = max(length, len(queue))
                while i in queue:
                    queue.pop(0)
            queue.append(i)

        return max(length, len(queue))


