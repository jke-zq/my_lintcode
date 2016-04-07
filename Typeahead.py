class Typeahead:

    # @param dict: A dictionary of words dict
    def __init__(self, dict):
        # do initialize if necessary
        # self.dict = dict
        # self.words = collections.defaultdict(list)
        # for word in dict:
        #     for w in word.split():
        #         self.words[w].append(word)
        # for key in self.words.keys():
        #     for words in self.dict:
        #         if key in words and words not in self.words[key]:
        #             self.words[key].append(words)
        
        self.words = collections.defaultdict(set)
        for word in dict:
            length = len(word)
            for i in range(length):
                for j in range(i + 1, length + 1):
                    s = word[i:j]
                    self.words[s].add(word)
        
        for k, v in self.words.items():
            self.words[k] = list(v)

    # @param word: a string
    # @return a list of words
    def search(self, word):
        # write your code here
        ### TLE
        # if self.words[word]:
        #     return self.words[word]
        # # else:
        # ans = list()
        # for w in self.dict:
        #     if word in w:
        #         ans.append(w)
        # if not ans:
        #     self.words[word] = ans
        # return ans
        if word in self.words:
            return self.words[word]
        else:
            return []

if __name__ == '__main__':
    dict = ["word_jci","word_g","word_mdon","word_b","word_krc","word_po","word_k","word_fj","word_m","word_pre","word_sehm","word_ahf","word_m","word_mdo","word_t","word_e","word_sl","word_c"]
    t = Typeahead(dict)

    print t.search("w")
    print t.search("o")
    print t.search("or")
    print t.search("word")
    print t.search("a")
    print t.search("bc")
    print t.search("d")
    print t.search("eq")
    print t.search("_")
    print t.search("list")
    print t.search("ad")
    print t.search("word_")
    print t.search("d_")
    print t.search("rd_ah")
    print t.search("word_a")
    print t.search("or")
    print t.search("o")
    print t.search("rd_")
    print t.search("d_t")
    print t.search("d_")
    print t.search("o")
    print t.search("or")
    print t.search("wo")
    print t.search("rd_m")
    print t.search("d_")
    print t.search("word_ahf")
    print t.search("r")
    print t.search("word")
    print t.search("word_")
    print t.search("_")
    print t.search("word_")
    print t.search("a")
    print t.search("ord_mdo")
    print t.search("jci")
    print t.search("word")
    print t.search("rd_s")
    print t.search("rd")
    print t.search("_m")
    print t.search("ord")
    print t.search("wor")
    print t.search("word_m")
    print t.search("ord")
    print t.search("rd")
    print t.search("wor")
    print t.search("rd_sl")
    print t.search("word_")
    print t.search("word")