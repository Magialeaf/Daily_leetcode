# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            if root:
                res.append(str(root.val))
                if root.left:
                    res.append("L")
                    dfs(root.left)
                if root.right:
                    res.append("R")
                    dfs(root.right)
            res.append("B")
            return

        dfs(root)
        return "".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = TreeNode(None)

        def dfs(root, idx):
            temp = []
            while idx < len(data):
                if data[idx] == "L":
                    if temp != []:
                        root.val = int("".join(temp))
                        temp = []
                    node = TreeNode()
                    root.left = node
                    idx = dfs(node, idx + 1)
                elif data[idx] == "R":
                    if temp != []:
                        root.val = int("".join(temp))
                        temp = []
                    node = TreeNode()
                    root.right = node
                    idx = dfs(node, idx + 1)
                elif data[idx] == "B":
                    if temp != []:
                        root.val = int("".join(temp))
                        temp = []
                    return idx + 1
                else:
                    temp.append(data[idx])
                    idx += 1

        if data == "B":
            return
        else:
            dfs(root, 0)
            return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))