#https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        s = {}
        for i in nums:
            if i not in s.keys():
                s[i] = 1
            else:
                s[i] = s[i] + 1
                return True
        return False

a = [1, 2, 3, 4]
ans = Solution()

print(ans.hasDuplicate(a))