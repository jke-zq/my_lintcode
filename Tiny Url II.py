class TinyUrl2:
    def __init__(self):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.carry = len(self.chars)
        self.charsDict = {key:index for index, key in enumerate(self.chars)}
        self.preUrl = "http://tiny.url/"
        self.shortToLongD = {}
        self.longToShortD = {}
        self.nextId = 0
        self.longToId = {}
        self.idToLong = {}
        
    def __idToShort(self, indexId):
        ans = ''
        while indexId > 0:
            ans = self.chars[indexId % self.carry] + ans
            indexId /= self.carry
        ans = self.chars[0] * (6 - len(ans)) + ans
        return ans
    
    def __shortToId(self, shortUrl):
        ans = 0
        for s in shortUrl:
            ans *= self.carry
            ans += self.charsDict[s]
        return ans
        
    # @param long_url a long url
    # @param a short key
    # @return a short url starts with http://tiny.url/
    def createCustom(self, long_url, short_key):
        # Write your code here
        if long_url in self.longToShortD and short_key != self.longToShortD[long_url]:
            return 'error' 
        if short_key in self.shortToLongD and self.shortToLongD[short_key] != long_url:
            return 'error'
        self.longToShortD[long_url] = short_key
        self.shortToLongD[short_key] = long_url
        return self.preUrl + short_key

    
    # @param {string} long_url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, long_url):
        # Write your code here
        if long_url in self.longToShortD:
            return self.preUrl + self.longToShortD[long_url]
        elif long_url in self.longToId:
            indexId = self.longToId[long_url]
            shortUrl = self.__idToShort(indexId)
            return self.preUrl + shortUrl
        else:
            shortUrl = self.__idToShort(self.nextId)
            self.idToLong[self.nextId] = long_url
            self.longToId[long_url] = self.nextId
            self.nextId += 1
            return self.preUrl + shortUrl
            
    # @param {string} short_url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, short_url):
        # Write your code here
        short_url = short_url.split(self.preUrl)[1]
        if short_url in self.shortToLongD:
            return self.shortToLongD[short_url]
        else:
            indexId = self.__shortToId(short_url)
            if indexId in self.idToLong:
                return self.idToLong[indexId]
            else:
                None
        
