# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        box = []
        max = 0
        for x in s:
            if x in box:
                fidx = box.index(x)
                box = box[fidx+1:]
                box.append(x)
            else:
                box.append(x)
            if len(box) > max:
                max = len(box)
        return max
