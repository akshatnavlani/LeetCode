class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map=defaultdict(int)
        for i in range (len(nums)):
            j = target - nums[i]
            if j in map.keys():
                k = int(map[j])
                return [k,i]
            map[nums[i]]+= i