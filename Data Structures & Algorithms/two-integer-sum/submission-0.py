class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            curr = target - num
            if curr in hashmap:
                return ([hashmap[curr], i])
            else:
                hashmap[num] = i


