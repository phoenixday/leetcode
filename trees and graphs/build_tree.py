class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#                           0 1 2 3 4 5 6
#    1            inorder:  4 2 5 1 6 3 7
#  2   3          preorder: 1 2 4 5 3 6 7
# 4 5 6 7
# 
#  if start != end : continue to left and right
#  left = [start, ind - 1] right = [ind + 1, end]
#  left_i = i + 1          right_i = i + 1 + ind - start
#  node = 1 i = 0 start = 0  end = 6  ind = 3  left_i = 1 right_i = 4
#  node = 2 i = 1 start = 0  end = 2  ind = 1  left_i = 2 right_i = 3
#  node = 4 i = 2 start = 0  end = 0  ind = 0  
#  node = 5 i = 3 start = 2  end = 2  ind = 2 
#  node = 3 i = 4 start = 4  end = 6  ind = 5  left_i = 5 right_i = 6
#  node = 6 i = 5 start = 4  end = 4  ind = 4
#  node = 7 i = 6 start = 6  end = 6  ind = 6


def build_tree(preorder: list[int], inorder: list[int], i=0, start=0, end=3000, dd: dict[int, int] = None) -> TreeNode | None:
    end = min(end, len(preorder) - 1)
    if not 0 <= start <= end < len(preorder):
        return None
    if not dd:
        dd = {v: i for i, v in enumerate(inorder)}
    node = TreeNode(preorder[i])
    mid = dd[preorder[i]]
    if end > start:
        node.left = build_tree(preorder, inorder, i + 1, start, mid - 1, dd)
        node.right = build_tree(preorder, inorder, i + 1 + mid - start, mid + 1, end, dd)
    return node


def check_tree(root: TreeNode | None, lst: list[int | None], i=0) -> bool:
    if i >= len(lst):
        return not root
    if not root:
        return lst[i] is None
    return root.val == lst[i] \
        and check_tree(root.left, lst, i * 2 + 1) \
        and check_tree(root.right, lst, i * 2 + 2)


def main():
    tests = [
        ([1,2,4,5,3,6,7], [4,2,5,1,6,3,7]),
        ([3,9,20,15,7], [9,3,15,20,7]),
        ([-1], [-1])
    ]
    expected = [
        [1,2,3,4,5,6,7],
        [3,9,20,None,None,15,7],
        [-1]
    ]
    for test, expected in zip(tests, expected):
        preorder, inorder = test
        assert check_tree(build_tree(preorder, inorder), expected)


if __name__ == "__main__":
    main()
