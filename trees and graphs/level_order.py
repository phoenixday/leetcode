import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None, level = 0, res: list[list[int]] = None) -> list[list[int]]:
    if res is None:
        res = []
    if root:
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        level_order(root.left, level + 1, res)
        level_order(root.right, level + 1, res)
    return res


def level_order_it(root: TreeNode | None) -> list[list[int]]:
    res, queue, i = [], [(root, 0)], 0
    while i < len(queue):
        node, level = queue[i]
        if node:
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        i += 1
    return res


def level_order_it2(root: TreeNode | None) -> list[list[int]]:
    res, queue, level = [], collections.deque([root]), 0
    while queue:
        # at the start, you will always have in the queue only current level nodes
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                queue.append(node.left)
                queue.append(node.right)
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
        [[3],[9,20],[15,7]],
        [],
        [[1]]
    ]
    for test, expected in zip(tests, expected):
        assert level_order_it2(convert_to_tree_node(test)) == expected

if __name__ == "__main__":
    main()
