### TLE
# import heapq
# class LFUCache:
#     class Node:
#         def __init__(self, k, v, freq):
#             self.k, self.v, self.freq = k, v, freq
#             self.next = None
#             self.pre = None
            
#     # @param capacity, an integer
#     def __init__(self, capacity):
#         # write your code here
#         self.storDict = {}
#         self.capacity = capacity
#         self.keyFreq = LFUCache.Node(-1, -1, -1)
#         self.leftCapacity = self.capacity

#     def sort(self, node):
#         if node.pre:
#             pre = node.pre
#             if node.next:
#                 node.next.pre = pre
#             else:
#                 return
#             pre.next = node.next
#         else:
#             pre = self.keyFreq
#         while pre.next and pre.next.freq <= node.freq:
#             pre = pre.next
#         node.pre = pre
#         node.next = pre.next
#         if pre.next:
#             pre.next.pre = node
#         pre.next = node
        
#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def set(self, key, value):
#         # write your code here
#         if key in self.storDict:
#             self.storDict[key].v = value
#             self.storDict[key].freq += 1
#             # heapq.heapify(self.keyFreq)
#             # self.keyFreq.sort(key = lambda x: x.freq)
#             self.sort(self.storDict[key])
#         else:
#             if self.leftCapacity == 0:
#                 delete = self.keyFreq.next
#                 self.storDict.pop(delete.k)
#                 delete.k, delete.v, delete.freq = key, value, 1
#                 self.storDict[delete.k] = delete
#                 self.sort(self.storDict[key])
#             else:
#                 self.leftCapacity -= 1
#                 new = LFUCache.Node(key, value, 1)
#                 # heapq.heappush(self.keyFreq, 
#                 # self.keyFreq.append(new)
#                 # self.keyFreq.sort(key = lambda x: x.freq)
#                 self.storDict[key] = new
#                 self.sort(self.storDict[key])
                

#     # @return an integer
#     def get(self, key):
#         # write your code here
#         if key in self.storDict:
#             node = self.storDict[key]
#             node.freq += 1
#             # self.keyFreq.remove(node)
#             # self.keyFreq.append(node)
#             # self.keyFreq.sort(key = lambda x: x.freq)
#             self.sort(self.storDict[key])
#             return node.v
#         else:
#             return -1