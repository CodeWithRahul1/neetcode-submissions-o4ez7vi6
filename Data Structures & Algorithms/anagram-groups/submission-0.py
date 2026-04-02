class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for char in strs:
            sorted_char = ''.join(sorted(char))
            if sorted_char not in res:
                res[sorted_char]=[]

            res[sorted_char].append(char)
        return list(res.values())

        