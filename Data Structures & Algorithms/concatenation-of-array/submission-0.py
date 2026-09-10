class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        input -> nums: 
        output -> ans: length: 2n
        [1,4,1,2]
        [0,0,0,0,0,0,0,0]
        i = 0
        i > 4 No [1,0,0,0,0,0,0,0]
        i=1
        i=2
        i=3
        i=4
        """
        ### What is n ?###
        n = len(nums)
        ### Create my array ###
        res = [0] * 2*n

        for i in range(2*n):
            if i > n - 1:
                idx_loc = i - n
                res[i] = nums[idx_loc]
            else:
                res[i] += nums[i]
        return res