class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1
        suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

        """
        [1,2,3,6]
        pre = [1,1,2,6]
        suff = [48,24,6,1]
        res = [0,0,0,0,0]

        pref[1] = nums[0] * pref[0] = 1*1 = 1
        pref[2] = nums[1] * pref[1] = 2 * 1 =  2
        pref[3] = nums[2] * pref[2] = 3 * 2 = 6
        pref[4] = nums[3] * pref[3] = 36

        suff[3] = nums[4] * suff[4] = 6 * 1 = 6
        """