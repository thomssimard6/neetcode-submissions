class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1_sorted = sorted(s)
        word2_sorted = sorted(t)
        if word1_sorted == word2_sorted:
            return True 
        else: 
            return False