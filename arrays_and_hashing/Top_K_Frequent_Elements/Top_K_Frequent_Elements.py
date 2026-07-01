class Solution:
    def topKFrequent(self, nums, k): # List[int], int -> List[int]
        a = {}
        for elem in nums:
            a[elem] = a.get(elem, 0) + 1
        
        b = {}
        for key in a.keys():
            l = b.get(a[key], [])
            l.append(key)
            b[a[key]] = l

        n = []
        for i in b.keys():
            n.append(i)

        n = sorted(n)

        m = []
        for i in n:
            m = [*m, *b[i]]
        return m[-k:]
    
nums = sorted(input().split()) # -1000 <= nums[i] <= 1000
k = int(input()) # 1 <= k <= number of distinct elements in nums

abs = Solution()
print(abs.topKFrequent(nums, k))