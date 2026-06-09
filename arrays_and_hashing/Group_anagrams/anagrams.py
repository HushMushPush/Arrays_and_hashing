# https://neetcode.io/problems/anagram-groups/question?list=neetcode150
class Solution:
    def groupAnagrams(self, strs): # List[str] -> List[List[str]]
        a = {}
        for elem in strs:
            key = ''.join(sorted(elem))
            if key not in a:
                a[key] = []
            a[key].append(elem)
                
        return list(a.values())
    

b = ["act","pots","tops","cat","stop","hat"]
ans = Solution()

print(ans.groupAnagrams(b))
