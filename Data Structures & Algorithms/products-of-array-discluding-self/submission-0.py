class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodarr=[]
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if(i!=j):
                    res=res*nums[j]
            prodarr.append(res)
        return prodarr