import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        while queue:
            node = queue.pop()
            print(node.data, end =' ')

            if node.left:
                queue.insert(False, node.left)
            if node.right:
                queue.insert(False, node.right)