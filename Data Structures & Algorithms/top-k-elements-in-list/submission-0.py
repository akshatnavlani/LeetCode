from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        maxval=max(x.values())
        bucket=[[] for i in range(maxval+1)]
        for num,count in x.items():
            bucket[count].append(num)
        res=[]
        for i in range(maxval,0,-1):
            bucket[i].sort(reverse=True)
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res