class Solution:
    def groupAnagrams(self, strs): # List[str] -> List[List[str]]
        a = {}
        for elem in strs:
            key = ''.join(sorted(elem))
            if key not in a:
                a[key] = []
            a[key].append(elem)
                
        return list(a.values())