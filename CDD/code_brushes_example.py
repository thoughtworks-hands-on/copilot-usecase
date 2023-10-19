class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
      
# Refactor and split the else part into a separate method
def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = minValue(root.right)
        root.right = deleteNode(root.right, root.key)
    
    return root

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.key, end=" ")
        inorderTraversal(root.right)

# Modify the insert values such that they form a degenerate binary tree
# Example usage:
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Inorder traversal before deletion:")
inorderTraversal(root)

key_to_delete = 30
root = deleteNode(root, key_to_delete)

print("\nInorder traversal after deleting", key_to_delete, ":")
inorderTraversal(root)
