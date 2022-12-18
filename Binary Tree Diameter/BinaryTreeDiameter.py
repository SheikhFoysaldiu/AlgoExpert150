# Binary Tree Diameter - Given a binary tree, find the length of its diameter.
# The diameter of a tree is the number of nodes on the longest path between any two leaf nodes.
# The diameter of a tree may or may not pass through the root.

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time Complexity: O(n) time | O(n) space


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)
    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


# Test
#        1
#      /   \
#     3     2
#    / \   / \
#   7   4 5   6
#  / \
# 8   9
tree = BinaryTree(1)
tree.left = BinaryTree(3)
tree.left.left = BinaryTree(7)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)
tree.left.right = BinaryTree(4)
tree.right = BinaryTree(2)
tree.right.left = BinaryTree(5)
tree.right.right = BinaryTree(6)
print(binaryTreeDiameter(tree))
