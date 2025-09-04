import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    res, queue, level = [], collections.deque([root]), 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft() if level % 2 == 0 else queue.pop()
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                if level % 2 == 0:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.appendleft(node.right)
                    queue.appendleft(node.left)
        level += 1
    return res


def convert_to_tree_node(lst: list[int | None], i=0) -> TreeNode | None:
    if len(lst) <= i or not lst[i]:
        return None
    return TreeNode(lst[i],
                    convert_to_tree_node(lst, i * 2 + 1),
                    convert_to_tree_node(lst, i * 2 + 2))


def main():
    tests = [
        [3,9,20,None,None,15,7],
        [],
        [1]
    ]
    expected = [
        [[3],[20,9],[15,7]],
        [],
        [[1]]
    ]
    for test, expected in zip(tests, expected):
        assert zigzag_level_order(convert_to_tree_node(test)) == expected

if __name__ == "__main__":
    main()
