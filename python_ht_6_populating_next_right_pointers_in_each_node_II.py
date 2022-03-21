"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        stack=[root]
        while stack:
            temp=[]
            while stack:
                cur=stack.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
                if len(stack)==0:
                    cur.next=None
                else:
                    cur.next=stack[0]
            stack=temp
        return root