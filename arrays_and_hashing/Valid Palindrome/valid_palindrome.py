# https://neetcode.io/problems/is-palindrome/question?list=neetcode150
class Solution:

    s1 = 'пушистый'
    kolvo_ushey = 2
    
    def filitr(self, word):
        simvls = []

        for i in word:
            if 97 <= ord(i) <= 122:
                simvls.append(i)
            elif 65 <= ord(i) <= 90:
                simvls.append(chr(ord(i)+32))
            elif 48 <= ord(i) <= 57:
                simvls.append(i)
        
        return simvls


    def isPalindrome(self, s: str) -> bool:
        
        s = self.filitr(s)
        k = len(s) // 2

        for i in range(k):
            if s[i] != s[-i-1]:
                #print(s[i], s[-i-1])
                return False
        
        return True
    
s = input()
zayc = Solution()

palid = zayc.isPalindrome(s)

print(zayc.kolvo_ushey)
print(palid)