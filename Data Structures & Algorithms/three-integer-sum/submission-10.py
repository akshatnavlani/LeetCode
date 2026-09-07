class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        seen=set()
        for curr in range(n-2):
            l,r=curr+1,n-1
            target=-(nums[curr])
            while l<r:
                lrsum=nums[l]+nums[r]
                append=[nums[curr],nums[l],nums[r]]
                if lrsum==target and tuple(append) not in seen:
                    res.append(append)
                    seen.add(tuple(append))
                elif lrsum<target:
                    l+=1
                else:
                    r-=1
        return res 