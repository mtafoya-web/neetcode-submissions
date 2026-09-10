class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = float("-inf")
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count +=1
        min_op = count
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                count +=1 
            if blocks[i - k] == 'W':
                count -= 1
            min_op = min(count, min_op)
        return min_op