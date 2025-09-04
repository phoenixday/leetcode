class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val < root.val < q.val or q.val < root.val < p.val:
        return root
    if p.val == root.val:
        return p
    if q.val == root.val:
        return q
    if p.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return None


# no tests
