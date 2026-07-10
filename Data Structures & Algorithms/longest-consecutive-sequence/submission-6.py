class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tup=list(sorted(set(nums)))
        if nums ==[]:
            return 0
        count=1
        i=0
        print(tup)
        for i in range(len(nums)):
            count_new=1
            while i<=(len(tup)-2) and  ((tup[i]+1 == tup[i+1]) or (tup[i]-1 == tup[i+1])):
                count_new+=1
                i+=1
            if count_new>count:
                count=count_new
        return count
            