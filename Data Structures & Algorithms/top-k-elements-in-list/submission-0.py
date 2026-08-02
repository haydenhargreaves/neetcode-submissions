class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        s = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        return list(s.keys())[:k]
        