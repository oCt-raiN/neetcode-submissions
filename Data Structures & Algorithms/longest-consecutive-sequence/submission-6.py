class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num = set(nums)
        max_count = 0
        visit = set()
        for i in nums:
            if i in visit:
                continue
            a = i
            count = 1 
            visit.add(i)
            while True:
                if a - 1 in num:
                    count += 1
                    a = a-1
                    visit.add(a)
                else:
                    break
            a = i
            while True:
                if a+1 in num:
                    count += 1
                    a = a+1
                    visit.add(a)
                else:
                    break
            max_count = max(max_count, count)
        return max_count