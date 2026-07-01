class Solution:
    def productExceptSelf(self, nums): # List[int] -> List[int]
        l_prefix = [1]
        r_prefix = [1]
        for i in range(len(nums)):
            l_prefix.append(nums[i]*l_prefix[i])
            r_prefix.append(nums[-i-1]*r_prefix[i])

        r_prefix = r_prefix[::-1]
        res = []

        for i in range(len(nums)):
            res.append(l_prefix[i]*r_prefix[i+1])
        
        return res
    
nums = [int(x) for x in input().split()]

abs = Solution()
print(abs.productExceptSelf(nums))