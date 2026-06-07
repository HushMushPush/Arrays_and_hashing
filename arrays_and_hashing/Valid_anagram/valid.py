#https://neetcode.io/problems/is-anagram/question?list=neetcode150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for elem in s:
            a[elem] = a.get(elem, 0) + 1
        for elem in t:
            b[elem] = b.get(elem, 0) + 1
        for key in a.keys():
            if key not in b.keys():
                return False
            elif a[key] != b[key]:
                return False
        for key in b.keys():
            if key not in a.keys():
                return False
            elif b[key] != a[key]:
                return False        
        return True
    
m = 'carcarcarxy'
n = 'carcarcar'

sol = Solution()

print(sol.isAnagram(m, n))