# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def populate_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while i < len(nodes):
            current = queue.pop(0)
            if nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1
        return root
    
    def print_tree(root, level=0, prefix="Root: ", is_left=None):
        if root is not None:
            print(" " * (level * 4) + prefix, end="")
            print(("|-- " if is_left else "\\-- ") + str(root.val))
            TreeNode.print_tree(root.left, level + 1, "L-- ", True)
            TreeNode.print_tree(root.right, level + 1, "R-- ", False)

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_root1 = Solution.findLeaf(root1, [])
        leaf_root2 = Solution.findLeaf(root2, [])
        if leaf_root1 == leaf_root2 :
            return True
        else :
            return False

    def findLeaf(root : TreeNode, leaf_root : list) -> list :
        if root.left is not None :
            Solution.findLeaf(root.left, leaf_root)
        if root.right is not None :
            Solution.findLeaf(root.right, leaf_root)
        if root.left is None and root.right is None :
            leaf_root.append(root.val)
        return leaf_root

   
nodes1 = [119, 113, None, 11, 30, 43, 76, 15, 60, 67, 74]
nodes2 = [11, 69, 60, 115, 66, 15, 60, 67, 74, None, 76]

root1 = TreeNode.populate_tree(nodes1)
root2 = TreeNode.populate_tree(nodes2)

rr = Solution()
print(rr.leafSimilar(root1, root2))