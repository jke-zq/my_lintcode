"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        if not root:
            return ""
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index]:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        # print queue
        while queue and queue[-1] is None:
            queue.pop()
        # print queue
        for i in range(len(queue)):
            if queue[i] is None:
                queue[i] = '#'
            else:
                queue[i] = queue[i].val
        return '|'.join([str(key) for key in queue])

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        # print data
        data = data.split('|')
        if not data:
            return None
        root = TreeNode(data.pop(0))
        queue = [root]
        while data:
            node = queue.pop(0)
            leftV = data.pop(0)
            if leftV == '#':
                node.left = None
            else:
                node.left = TreeNode(int(leftV))
                queue.append(node.left)
            if data:
                rightV = data.pop(0)
                if rightV == '#':
                    node.right = None
                else:
                    node.right = TreeNode(int(rightV))
                    queue.append(node.right)
        return root
                    
        