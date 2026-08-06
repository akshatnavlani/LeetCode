class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr=[]
        count=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while arr!=[] and temperatures[arr[-1]]<temp:
                s=arr.pop()
                count[s]=i-s
            arr.append(i)
        return count