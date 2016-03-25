class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        if not chars:
            return None
        
        length = len(chars)
        left, pivot, right = 0, 0, length - 1
        while left <= right:
            if chars[left].islower():
                chars[pivot], chars[left] = chars[left], chars[pivot]
                pivot += 1
                left += 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                right -= 1
        
