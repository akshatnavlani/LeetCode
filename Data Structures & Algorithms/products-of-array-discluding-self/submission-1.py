class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodarr=[0]*len(nums)
        count0=0
        res=1
        for i in nums:
            if i!=0:
                res=res*i
            else: 
                count0+=1
        if count0>1:
            return prodarr
        if count0==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    prodarr[i]=res
            return prodarr
        if count0==0:
            prodarr=[res]*len(nums)
            for i in range(len(nums)):
                prodarr[i]=res//nums[i]
            return prodarr
                

