class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num = set(nums)
        max_count = 0
        while num:
            count = 1
            a = num.pop()
            i = a
            while True:
                if a- 1 in num:
                    count += 1
                    num.remove(a -1)
                    a = a -1 
                else:
                    break
            a = i
            while True:
                if  a+ 1 in num:
                    count += 1
                    num.remove(a+1)
                    a = a+1
                else:
                    break
            max_count = max(max_count,count)
        return max_count