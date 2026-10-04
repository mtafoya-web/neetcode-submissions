class Solution:
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the '#' delimiter that marks the end of the length integer
            j = i
            while s[j] != '#':
                j += 1
            
            # Parse the length of the string
            length = int(s[i:j])
            
            # Slice the string of specified length starting right after '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move index to the beginning of the next encoded string
            i = end
            
        return res