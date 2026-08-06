import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print('-11'.isdigit())
        operator_mapping = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        arr=[]
        for i in tokens:
            if i in operator_mapping:
                a=arr.pop()
                b=arr.pop()
                calculation=operator_mapping[i]
                res=calculation(int(b),int(a))
                arr.append(res)
            else:
                arr.append(int(i))
        return int(arr[0])

            