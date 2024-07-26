class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [num for num in nums if nums.count(num) == 1][0]
