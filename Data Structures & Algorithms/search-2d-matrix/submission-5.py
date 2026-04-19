class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix) - 1
        lr, rr = 0, nr
        
        while lr <= rr:
            m = lr + (rr - lr) // 2
            if matrix[m][0] > target:
                rr = m - 1
            elif matrix[m][-1] < target:
                lr = m + 1
            else:
                lc, rc = 0, len(matrix[m]) - 1
                while lc <= rc:
                    mc = lc + (rc - lc) // 2
                    if matrix[m][mc] > target:
                        rc = mc - 1
                    elif matrix[m][mc] < target:
                        lc = mc + 1
                    else:
                        return True
                return False
        return False

