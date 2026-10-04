class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ### if sorted we can just check the last and first element ###
        ### Two Pointer ###
        if len(numbers) < 2:
            return None
        
        front = 0
        back = len(numbers) - 1

        while front < back:
            curr_sum = numbers[front] + numbers[back]
            if curr_sum < target:
                front += 1
            elif curr_sum > target:
                back -= 1
            else:
                return [front + 1, back + 1]
        return []