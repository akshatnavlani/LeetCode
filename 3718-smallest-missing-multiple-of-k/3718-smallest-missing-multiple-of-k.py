class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=len(nums)
        last=0
        for i in range(1,n+1):
            if k*i in nums:
                last+=1
                continue
            else:
                return k*i
        return (last+1)*k