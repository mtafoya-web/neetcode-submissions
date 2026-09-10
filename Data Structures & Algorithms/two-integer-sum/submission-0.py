class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #{num: idx}

        for idx in range(len(nums)):
            compl = target - nums[idx]
            if compl in hashmap:
                return [hashmap[compl], idx]
            hashmap[nums[idx]] = idx
        


