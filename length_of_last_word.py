# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()
        word = s.split(' ')
        last_idx = len(word) - 1
        return len(word[last_idx])
