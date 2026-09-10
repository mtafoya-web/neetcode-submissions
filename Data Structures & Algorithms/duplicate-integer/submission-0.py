class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict() ### {num: 1/0}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        return False 
        