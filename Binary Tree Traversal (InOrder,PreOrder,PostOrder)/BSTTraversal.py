class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Inorder
def inOrderTraversal(tree,array):
    if tree is not None:
        inOrderTraversal(tree.left,array)
        array.append(tree.value)
        inOrderTraversal(tree.right,array)
    return array



#Preorder
def preOrderTraversal(tree,array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraversal(tree.left,array)
        preOrderTraversal(tree.right,array)
    return array


#Postorder

def postOrderTraversal(tree,array):
    if tree is not None:
        postOrderTraversal(tree.left,array)
        postOrderTraversal(tree.right,array)
        array.append(tree.value)
    return array

# Time Complexity: O(n) where n is the number of nodes in the binary tree.
# Test
#              1
#            /   \
#           2     3
#          / \   / \
#         4   5 6   7
#            /       
#           8                  


# Driver Code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("Inorder Traversal of binary tree is")
    print(inOrderTraversal(root,[]))
    print("Preorder Traversal of binary tree is")
    print(preOrderTraversal(root,[]))
    print("Postorder Traversal of binary tree is")
    print(postOrderTraversal(root,[]))

# Output
# Inorder Traversal of binary tree is
# [4, 2, 8, 5, 1, 6, 3, 7]
# Preorder Traversal of binary tree is
# [1, 2, 4, 5, 8, 3, 6, 7]
# Postorder Traversal of binary tree is
# [4, 8, 5, 2, 6, 7, 3, 1]
