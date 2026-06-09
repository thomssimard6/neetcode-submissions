class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = {}
        for i in nums:
            most_frequent[i] = most_frequent.get(i, 0) + 1
        arr = []
        for i, cnt in most_frequent.items():
            arr.append([cnt, i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        

