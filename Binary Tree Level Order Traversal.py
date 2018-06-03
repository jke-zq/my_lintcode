"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            curLevel = []
            for __ in range(len(queue)):
                node = queue.popleft()
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curLevel)
        return ans
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        # if root is None:
        #     return []
        # ans, queue = [], [root]
        # index, length = 0, 1
        # while index < length:
        #     tmp = []
        #     for i in range(index, length):
        #         cur = queue[index]
        #         tmp.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #             length += 1
        #         if cur.right:
        #             queue.append(cur.right)
        #             length += 1
        #         index += 1
        #     ans.append(tmp)
        # return ans
        def dfs(node, tmp, cur_level, max_level):
            if node is None:
                return
            if cur_level == max_level:
                tmp.append(node.val)
                return
            dfs(node.left, tmp, cur_level + 1, max_level)
            dfs(node.right, tmp, cur_level + 1, max_level)

        ans = []
        if root is None:
            return ans
        max_level = 0
        while True:
            tmp = []
            dfs(root, tmp, 0, max_level)
            if tmp == []:
                break
            ans.append(tmp)
            max_level += 1

        return ans

