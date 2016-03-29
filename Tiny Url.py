class TinyUrl:
    # @param {string} url a long url
    # @return {string} a short url
    CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    CARRY = len(CHARS)
    CHARSDICT = {key:index for index, key in enumerate(CHARS)}
    PREURL = "http://tiny.url/"
    def __init__(self):
        self.urlToId = {}
        self.idToUrl = {}
        self.nextId = 0
    
    def __shortUrlToId(self, shortUrl):
        ans = 0
        for s in shortUrl:
            ans *= 62
            ans += TinyUrl.CHARSDICT[s]
        return ans
        
    def __idToShortUrl(self, indexId):
        ans = ""
        while indexId > 0:
            ans = TinyUrl.CHARS[indexId % 62] + ans
            indexId /= TinyUrl.CARRY
        ans = TinyUrl.CHARS[0] * (6 - len(ans)) + ans
        return ans
        
    def longToShort(self, url):
        # Write your code here
        if url in self.urlToId:
            return TinyUrl.PREURL + self.__idToShortUrl(self.urlToId[url])
        else:
            ans = self.__idToShortUrl(self.nextId)
            ans = TinyUrl.PREURL + ans
            self.urlToId[url] = self.nextId
            self.idToUrl[self.nextId] = url
            self.nextId += 1
            # print self.nextId, ans
            return ans

    # @param {string} url a short url
    # @return {string} a long url
    def shortToLong(self, url):
        # Write your code here
        # url = url.split('')[1]
        indexId = self.__shortUrlToId(url)
        if indexId in self.idToUrl:
            return self.idToUrl[indexId]
        else:
            return None