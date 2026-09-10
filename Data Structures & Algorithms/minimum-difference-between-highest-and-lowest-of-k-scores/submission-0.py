class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #Sliding window
        nums.sort()
        diff = float("inf")
        for i in range(len(nums) - k + 1):
            min_diff = nums[i + k - 1] - nums[i]
            if min_diff < diff:
                diff = min_diff
        return diff
        