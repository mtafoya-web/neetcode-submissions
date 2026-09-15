class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        An anagram is a word using the same letters as another word
        For Example, racecar and carrace are anagrams
        Intution : Iterate through letters and count the number of times a character appears
        we can do these mappings using a hashmap
        """

        ### PsuedoCode ###
        # Lengths have to be equal
        if len(s) != len(t): return False
        # Track the letters in s and t using a dict#
        s_seen = dict()
        t_seen = dict()
        # iterate through the dictionary and count the number of values in a dict
        for char_s, char_t in zip(s, t):
            s_seen[char_s] = s_seen.get(char_s, 0) + 1
            t_seen[char_t] = t_seen.get(char_t, 0) + 1
        
        for key, value in s_seen.items():
            if key not in t_seen or t_seen[key] != s_seen[key]:
                return False
        return True 
        # iterate through the dictionary and remove all the letters that have been seen
        # if the count of any of the letters is not the same return False otherwise return True
