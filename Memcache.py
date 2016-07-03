class Resource:
    def __init__(self, val, expired):
        self.val = val
        self.expired = expired

INT_MAX = 2147483647


class Memcache:

    def __init__(self):
        # initialize your data structure here.
        self.client = {}

    # @param {int} curt_time an integer
    # @param {int} key an integer
    # @return an integer
    def get(self, curt_time, key):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        re = self.client[key]
        if re.expired >= curt_time or re.expired == -1:
            return re.val
        else:
            return INT_MAX

    # @param {int} curt_time an integer
    # @param {int} key an integer
    # @param {int} value an integer
    # @param {int} ttl an integer
    # @return nothing
    def set(self, curt_time, key, value, ttl):
        # Write your code here
        # if key not in self.client:
        #     re = Resource(value, 0)
        #     self.client[key] = re
        # re = self.client[key]
        # re.val = value
        # if ttl == 0:
        #     re.expired = -1
        # else:
        #     re.expired = curt_time + ttl - 1
        re = Resource(value, 0)
        if ttl == 0:
            re.expired = -1
        else:
            re.expired = curt_time + ttl - 1
        self.client[key] = re

    # @param {int} curt_time an integer
    # @param {int} key an integer
    # @return nothing
    def delete(self, curt_time, key):
        # Write your code here
        if key not in self.client:
            return
        del self.client[key]

    # @param {int} curt_time an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def incr(self, curt_time, key, delta):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        self.client[key].val += delta
        return self.get(curt_time, key)

    # @param {int} curt_time an integer
    # @param {int} key an integer
    # @param {int} delta an integer
    # @return an integer
    def decr(self, curt_time, key, delta):
        # Write your code here
        if key not in self.client:
            return INT_MAX
        self.client[key].val -= delta
        return self.get(curt_time, key)
