import threading
class Solution:
    # @return: The same instance of this class every time
    instance = None
    mutex = threading.Lock()
    @classmethod
    def getInstance(cls):
        # write your code here
        # if cls.instance is None:
        #     cls.instance = Solution()
        # return cls.instance
        
        if cls.instance is None:
            cls.mutex.acquire()
            if cls.instance is None:
                cls.instance = cls()
            cls.mutex.release()
        
        return cls.instance