class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        
        def getRowMaxIndex(A, mid, cLeft, cRight):
            ans = -1
            maxV = float('-inf')
            for i in range(cLeft, cRight + 1):
                if maxV < A[mid][i]:
                    maxV = A[mid][i]
                    ans = i
            return ans
        def getColMaxIndex(A, rUp, rDown, col):
            ans = -1
            maxV = float('-inf')
            for i in range(rUp, rDown + 1):
                if maxV < A[i][col]:
                    maxV = A[i][col]
                    ans = i
            return ans
                
        if not A or not A[0]:
            return None
        
        Rows = len(A)
        Cols = len(A[0])
        
        rUp, rDown, cLeft, cRight = 0, Rows - 1, 0, Cols - 1
        mid = rUp + (rDown - rUp) / 2
        while rUp + 1 < rDown:
            rowMaxIndex = getRowMaxIndex(A, mid, cLeft, cRight)
            if A[mid][rowMaxIndex] < A[mid + 1][rowMaxIndex]:
                rUp = mid
            elif A[mid][rowMaxIndex] < A[mid - 1][rowMaxIndex]:
                rDown = mid
            else:
                return [mid, rowMaxIndex]
            
            colMaxIndex = getColMaxIndex(A, rUp, rDown, rowMaxIndex)
            if A[colMaxIndex][rowMaxIndex] < A[colMaxIndex][rowMaxIndex - 1]:
                cRight = rowMaxIndex
            elif A[colMaxIndex][rowMaxIndex] < A[colMaxIndex][rowMaxIndex + 1]:
                cLeft = rowMaxIndex
            else:
                return [colMaxIndex, rowMaxIndex]
            mid = colMaxIndex
                