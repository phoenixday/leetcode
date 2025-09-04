import math
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None, minn = -math.inf, maxx = math.inf) -> bool:
    if not root:
        return True
    if not minn <= root.val <= maxx:
        return False
    return is_valid_bst(root.left, minn, root.val - 1) \
        and is_valid_bst(root.right, root.val + 1, maxx)


def is_valid_bst_dfs(root: TreeNode | None) -> bool:
    stack = collections.deque([(root, -math.inf, math.inf)])
    while stack:
        node, minn, maxx = stack.pop()
        if node:
            if not minn <= node.val <= maxx:
                return False
            stack.append((node.left, minn, node.val - 1))
            stack.append((node.right, node.val + 1, maxx))
    return True


def is_valid_bst_inorder(root: TreeNode | None) -> bool:
    last = -math.inf
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if last >= curr.val:
            return False
        last = curr.val
        curr = curr.right
    return True


def is_valid_bst_inorder_rec(root: TreeNode | None, last = None) -> bool:
    if not root:
        return True
    if not last:
        last = [-math.inf]
    if not is_valid_bst_inorder_rec(root.left, last) or last[0] >= root.val:
        return False
    last[0] = root.val
    return is_valid_bst_inorder_rec(root.right, last)


#         0               
#    1          2       
#  3   4     5     6    
# 7 8 9 10 11 12 13 14   
def convert_to_tree_node(lst: list[int | None], i=0) -> TreeNode | None:
    if len(lst) <= i or not lst[i]:
        return None
    return TreeNode(lst[i],
                    convert_to_tree_node(lst, i * 2 + 1),
                    convert_to_tree_node(lst, i * 2 + 2))


def main():
    tests = [
        [2,1,3],
        [5,1,4,None,None,3,6],
        [5,4,6,None,None,3,7],
        [1,None,1],
        [1,1]
    ]
    expected = [
        True,
        False,
        False,
        False,
        False
    ]
    for test, expected in zip(tests, expected):
        assert is_valid_bst_inorder_rec(convert_to_tree_node(test)) == expected

if __name__ == "__main__":
    main()
