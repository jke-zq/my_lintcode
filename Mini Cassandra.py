# """
# Definition of Column:
# class Column:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
# """
# import collections
# class MiniCassandra:

#     def __init__(self):
#         # initialize your data structure here.
#         self.tables = collections.defaultdict(list)
#         self.data = {}


#     # @param {string} raw_key a string
#     # @param {int} column_key an integer
#     # @param {string} column_value a string
#     # @return nothing
#     def insert(self, raw_key, column_key, column_value):
#         # Write your code here
#         self.tables[raw_key].append(column_key)
#         self.data[column_key] = column_value

#     # @param {string} raw_key a string
#     # @param {int} column_start an integer
#     # @param {int} column_end an integer
#     # @return {Column[]} a list of Columns
#     def query(self, raw_key, column_start, column_end):
#         # Write your code here
#         import bisect
#         self.tables[raw_key].sort()
#         table = self.tables[raw_key]
#         start = bisect.bisect_left(table, column_start)
#         end = bisect.bisect_right(table, column_end)
#         # print table, start, end
#         ans = [(key, str(self.data[key])) for key in table[start:end]]
#         # print ans
#         # print 
#         # print "[%s]" % ','.join(['%s' % item for item in ans]) 
#         return ans

import collections
class Column:
    def __init__(self, key, value):
        self.key = key
     
class MiniCassandra:

    def __init__(self):
        # initialize your data structure here.
        self.tables = collections.defaultdict(dict)


    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
    def insert(self, raw_key, column_key, column_value):
        # Write your code here
        self.tables[raw_key][column_key] = Column(column_key, column_value)

    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns
    def query(self, raw_key, column_start, column_end):
        # Write your code here
        ans = []
        for k, v in self.tables.get(raw_key, {}).items():
            if k >= column_start and k <= column_end:
                ans.append(v)
        ans.sort(lambda x: x.key)
        return ans
        

if __name__ == '__main__':
    a = MiniCassandra()
    a.insert("google", 1, "haha")
    a.query("google", 0, 1)