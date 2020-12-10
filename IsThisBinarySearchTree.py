""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return helper(root, -1, 10001)

def helper(root, min, max):
    if root == None:
        return True

    if min > root.data:
        return False
    if max < root.data:
        return False

    return helper(root.left, min, root.data - 1) and helper(root.right, root.data + 1, max)