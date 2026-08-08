class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lv,rv=0,len(matrix)-1
        while lv<=rv:
            lh,rh=0,len(matrix[0])-1
            midv=(rv+lv)//2
            while lh<=rh:
                midh=(rh+lh)//2
                if matrix[midv][midh]==target:
                    return True
                elif target > matrix[midv][midh]:
                    lh=midh+1
                else:
                    rh=midh-1
            if target > matrix[midv][midh]:
                lv=midv+1
            else:
                rv=midv-1
        return False