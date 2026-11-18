class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = [1] * len(nums)
        nums.sort()
        d = {nums[i] : i for i in range(len(nums))}
        # print(d)
        for i in range(len(nums)): 
            if nums[i] - 1 in d:
                loc = d[nums[i] - 1]
                res[i] = res[loc] + 1 
            else:
                continue
        # print(res)
        return max(res)