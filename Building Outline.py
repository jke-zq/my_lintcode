import heapq


class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        # write your code here

        if not buildings:
            return []
        builds = []
        for x, y, h in buildings:
            builds.append((x, -1 * h, 0))
            builds.append((y, h, 1))
        
        builds.sort()
        maxheap = []
        ret = []
        for x, h, t in builds:
            # start
            if t == 0:
                if not maxheap:
                    ret.append([x, x, -1 * h])
                elif maxheap[0] > h:
                    ret[-1][1] = x
                    ret.append([x, x, -1 * h])
                heapq.heappush(maxheap, h)
            elif t == 1:  # end
                maxheap.remove(-1 * h)
                if not maxheap:
                    ret[-1][1] = x
                    # if ret[-1][0] == ret[-1][1]:
                    #     ret.pop()
                else:
                    heapq.heapify(maxheap)
                    if -1 * maxheap[0] < h:
                        ret[-1][1] = x
                        ret.append([x, x, -1 * maxheap[0]])
        return ret
