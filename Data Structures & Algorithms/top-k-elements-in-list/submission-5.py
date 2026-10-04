"""
Understand:
    Input: list[int], int: k
    output: list[int] -> list contains the k numbers that appear most frequently
    edge: no frequent elements -> return [], 
Match:
    Hashmap -> stores the frequency
Plan:
    1. if len < 1 -> return empty list
    2. populate the frequency map
    3. sort by count
    4. return the k most frequent keys
Implement:
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        return sorted(hashmap, key=hashmap.get, reverse=True)[0:k]
        