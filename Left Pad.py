class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        length = len(originalStr)
        if length >= size:
            return originalStr
        else:
            padList = [padChar] * (size - length)
            return ''.join(padList) + originalStr