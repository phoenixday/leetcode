import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode | None, res: list[int] = None) -> list[int]:
    if res is None:
        res = []
    if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)
    return res


def inorder_traversal_it(root: TreeNode | None) -> list[int]:
    res = []
    stack = collections.deque([(root, False)])
    while stack:
        node, left_visited = stack.pop()
        if node:
            if not left_visited:
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                res.append(node.val)
                stack.append((node.right, False))
    return res


def inorder_traversal_it2(root: TreeNode | None) -> list[int]:
    res = []
    stack = collections.deque()
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def convert_to_tree_node(lst: list[int | None], i=0) -> TreeNode | None:
    if len(lst) <= i or not lst[i]:
        return None
    return TreeNode(lst[i],
                    convert_to_tree_node(lst, i * 2 + 1),
                    convert_to_tree_node(lst, i * 2 + 2))


def main():
    tests = [
        [1,None,2,None,None,3],
        [1,2,3,4,5,None,8,None,None,6,7,None,None,9],
        [],
        [1]
    ]
    expected = [
        [1,3,2],
        [4,2,6,5,7,1,3,9,8],
        [],
        [1]
    ]
    for test, expected in zip(tests, expected):
        assert inorder_traversal(convert_to_tree_node(test)) == expected

if __name__ == "__main__":
    main()
