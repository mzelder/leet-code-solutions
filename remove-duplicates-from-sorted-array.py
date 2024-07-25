class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1:
            j = i + 1
            while j < n:
                if nums[i] == nums[j]:
                    del nums[j]
                    n -= 1
                else:
                    j += 1
            i += 1

        return len(nums)