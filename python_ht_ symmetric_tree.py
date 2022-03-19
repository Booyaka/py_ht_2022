class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        stack = collections.deque([(root.left, root.right)])
        while stack:
            l, r = stack.popleft()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True