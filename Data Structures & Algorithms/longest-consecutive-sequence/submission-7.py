class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums=sorted(set(nums))
        print(nums)
        res=0
        curr,streak=nums[0],0
        i=0
        while i<len(nums):
            if nums[i]!=curr:
                curr=nums[i]
                streak=0
            i+=1
            streak+=1
            curr+=1
            res=max(res,streak)
            print(res)
        return res
            