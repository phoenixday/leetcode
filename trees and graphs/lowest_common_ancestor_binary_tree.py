import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None
    if root.val in [p.val, q.val]:
        return root
    res_left = lowest_common_ancestor(root.left, p, q)
    res_right = lowest_common_ancestor(root.right, p, q)
    if res_left and res_right:
        return root
    return res_left if res_left else res_right


def convert_to_tree(lst: list[int | None], p_val: int, q_val: int, i=0) \
    -> tuple[TreeNode, TreeNode, TreeNode]:
    if len(lst) <= i or not lst[i]:
        return (None, None, None)
    root, p, q = TreeNode(lst[i]), None, None
    root.left, p_left, q_left = convert_to_tree(lst, p_val, q_val, i * 2 + 1)
    root.right, p_right, q_right = convert_to_tree(lst, p_val, q_val, i * 2 + 2)
    p = root if root.val == p_val else (p_left if p_left else p_right)
    q = root if root.val == q_val else (q_left if q_left else q_right)
    return root, p, q


def main():
    tests = [
        ([3,5,1,6,2,0,8,None,None,7,4], 5, 1),
        ([3,5,1,6,2,0,8,None,None,7,4], 5, 4),
        ([1,2], 1, 2)
    ]
    expected = [
        3,
        5,
        1
    ]
    for test, expected in zip(tests, expected):
        lst, p_val, q_val = test
        tree, p, q = convert_to_tree(lst, p_val, q_val)
        res = lowest_common_ancestor(tree, p, q)
        assert res.val == expected

if __name__ == "__main__":
    main()
