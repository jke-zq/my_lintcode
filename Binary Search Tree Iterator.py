"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        # self.nodes = []
        # node = root
        # while node:
        #     self.nodes.append(node)
        #     node = node.left
        self.curt = root
        self.stack = []

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        # return self.nodes != []
        return self.curt or self.stack

    #@return: return next node
    def next(self):
        #write your code here
        # node = self.nodes.pop()
        # if node.right:
        #     p = node.right
        #     while p:
        #         self.nodes.append(p)
        #         p = p.left
        # return node
        while self.curt:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        self.curt = self.stack.pop()
        val = self.curt
        self.curt = self.curt.right
        return val