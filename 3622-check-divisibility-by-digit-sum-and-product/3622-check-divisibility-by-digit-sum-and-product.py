class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        prod=1
        new=n
        while new !=0:
            sum+=new%10
            prod*=new%10
            new=new//10
        total=sum+prod
        print(total)
        if n%total==0:
            return True
        return False
