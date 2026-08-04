class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                missing.append(i)
        return missing