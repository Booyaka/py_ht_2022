# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack, p_trace, q_trace = [], [], []

        while True:
            if root.left:
                stack.append(root)
                root.left, root = None, root.left
            elif root.right:
                stack.append(root)
                root.right, root = None, root.right
            else:
                if root is p:
                    p_trace = stack[:]
                    p_trace.append(root)
                if root is q:
                    q_trace = stack[:]
                    q_trace.append(root)
                if p_trace and q_trace:
                    break
                root = stack.pop()

        i, m = 0, min(len(p_trace), len(q_trace))
        while i < m and p_trace[i] is q_trace[i]:
            ans = p_trace[i]
            i += 1
        return ans