class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map=defaultdict(list)
        for i in range (len(nums)):
            j = target - nums[i]
            if j in map.keys():
                k = map[j]
                l=int(k[0])
                arr=[i,l]
                return sorted(arr)
            map[nums[i]]+= str(i)
        


