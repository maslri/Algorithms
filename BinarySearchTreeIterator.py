# https://leetcode.com/problems/binary-search-tree-iterator/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]) -> None:
        self.stack = []
        self._inorder_leftmost(root)

    def _inorder_leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if not self.hasNext():
            return None

        current_node = self.stack.pop()
        self._inorder_leftmost(current_node.right)

        return current_node.val

    def hasNext(self) -> bool:
        return bool(self.stack)


tree = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
iterator = BSTIterator(tree)

print(iterator.next())    # Output: 3
print(iterator.next())    # Output: 7
print(iterator.hasNext()) # Output: True
print(iterator.next())    # Output: 9
print(iterator.hasNext()) # Output: True
print(iterator.next())    # Output: 15
print(iterator.hasNext()) # Output: True
print(iterator.next())    # Output: 20
print(iterator.hasNext()) # Output: False