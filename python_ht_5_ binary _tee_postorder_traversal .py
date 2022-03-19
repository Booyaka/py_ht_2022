class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [(root, False)]
        result = []
        while stack:
            node, done = stack.pop()
            if done:
                result.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return result