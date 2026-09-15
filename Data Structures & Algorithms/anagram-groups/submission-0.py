class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### Sublists ###
        """
        act, pots, tops, cat, stop, hat
        [act]:[cat, hat]
        Find the anagrams of a letter
        There are 26 letters in the alphabet using the ordinance(lower case letters)
        """

        ### list that acts like a storage using the ordnance###
        anagrams = dict()

        for word in strs:
            alphabet = [0] * 26
            ### Gives us the index of the letter ###
            for letter in word:
                idx = ord(letter) - ord('a')
                alphabet[idx] += 1
            key = tuple(alphabet)
            if key not in anagrams: anagrams[key] = []
            anagrams[key].append(word)

        
        return list(anagrams.values())