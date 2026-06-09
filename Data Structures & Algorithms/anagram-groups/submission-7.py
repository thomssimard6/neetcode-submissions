class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nums = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            nums[sortedS].append(s)
        return list(nums.values())