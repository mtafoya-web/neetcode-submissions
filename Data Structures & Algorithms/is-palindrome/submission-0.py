class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Understand -> input s, output bool, edge empty list, list of one element
        Map -> Two pointer
        Plan ->
            1. Check for empty list
            2. INIT pointers
            3. while loop -> while front < back
            4. check if element is different -> return False
            5. Exit loop -> return True
        Implement -> 
        Results -> 
        Evaluate ->
        """
        if len(s) < 1:
            return False
        
        front = 0
        back = len(s) - 1
        while front < back:
            while front < back and not s[front].isalnum():
                front += 1
            while front < back and not s[back].isalnum():
                back -= 1
            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
        return True
        