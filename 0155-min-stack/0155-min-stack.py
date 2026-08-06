class MinStack:

    def __init__(self):
        self.arr=[]

    def push(self, val: int) -> None:
        if self.arr==[]:
            self.arr.append([val,val])
        else:
            mini=min(self.arr[-1][1],val)
            self.arr.append([val,mini])
    def pop(self) -> None:
        self.arr.pop()
    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
