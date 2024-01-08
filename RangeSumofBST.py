# https://leetcode.com/problems/range-sum-of-bst/?envType=daily-question&envId=2024-01-08

# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class calculate :

    def __init__(self, root : TreeNode) -> None:
        self.root = root
    
    def findRange(self, low : int, high : int) -> list:
        result = []
        stack = [self.root]

        while stack:
            current_node = stack.pop()

            if current_node:
                if low <= current_node.val <= high:
                    result.append(current_node.val)

                if current_node.val > low:
                    stack.append(current_node.left)

                if current_node.val < high:
                    stack.append(current_node.right)

        return result

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        calc = calculate(root)
        return sum(calc.findRange(low, high))

# Example usage:
# Construct the tree
# [10,5,15,3,7,null,18]
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right.right = TreeNode(18)
rr1 = Solution()
# Test case 1
print(rr1.rangeSumBST(root1, 7, 15))  # Output: 32

# Construct another tree
# [10,5,15,3,7,13,18,1,null,6]
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)
root2.left.left.left = TreeNode(1)
root2.left.right.left = TreeNode(6)
rr2 = Solution()
# Test case 2
print(rr2.rangeSumBST(root2, 6, 10))  # Output: 23