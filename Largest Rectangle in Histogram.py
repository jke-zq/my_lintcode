class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0
        
        length = len(height)
        stack = []
        ans = float('-inf')
        for i in range(length + 1):
            if i == length:
                val = -1
            else:
                val = height[i]
            if not stack or height[stack[-1]] <= val:
                stack.append(i)
            else:
                while stack and height[stack[-1]] > val:
                    cur = stack.pop()
                    last = -1 if not stack else stack[-1]
                    ans = max(ans, height[cur] * (i - last - 1))
                stack.append(i)
        return ans
                    
        