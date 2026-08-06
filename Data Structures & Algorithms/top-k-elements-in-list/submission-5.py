class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in count_dict.items():
            bucket[value].append(key)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result