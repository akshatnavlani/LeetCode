class Solution:
    def binarySearch(self,l:int,r:int,nums:List[int],target:int)->int:
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l
        result=self.binarySearch(0,pivot-1,nums,target)
        if result!=-1:
            return result
        return self.binarySearch(pivot,len(nums)-1,nums,target)
