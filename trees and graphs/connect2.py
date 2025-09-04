class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next_node: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_node


def find_next_child(node: Node | None) -> Node | None:
    if not node:
        return None
    if node.left:
        return node.left
    if node.right:
        return node.right
    return find_next_child(node.next)


def find_leftmost(node: Node | None) -> Node | None:
    if not node:
        return None
    if node.left:
        return node.left
    if node.right:
        return node.right
    return find_leftmost(node.next)


def connect(root: Node | None) -> Node | None:
    leftmost = root
    while leftmost:
        curr = leftmost
        while curr:
            if curr.left:
                curr.left.next = curr.right if curr.right else find_next_child(curr.next)
            if curr.right:
                curr.right.next = find_next_child(curr.next)
            curr = curr.next
        leftmost = find_leftmost(leftmost)
    return root


def convert_to_tree(lst: list[int | None], i=0) -> Node | None:
    if len(lst) <= i or not lst[i]:
        return None
    return Node(lst[i],
                    convert_to_tree(lst, i * 2 + 1),
                    convert_to_tree(lst, i * 2 + 2))


def get_nexts(root: Node | None) -> list[int | None]:
    res, leftmost = [], root
    while leftmost:
        curr = leftmost
        while curr:
            res.append(curr.val)
            curr = curr.next
        res.append(None)
        leftmost = leftmost.left
    return res


def main():
    tests = [
        [1, 2, 3, 4, 5,None,7],
        [],
        [1,2,3,4,5,None,6,7,None,None,None,None,None,None,8]
    ]
    expected = [
        [1,None,2,3,None,4,5,7,None],
        [],
        [1,None,2,3,None,4,5,6,None,7,8,None]
    ]
    for test, expected in zip(tests, expected):
        tree = convert_to_tree(test)
        connect(tree)
        assert get_nexts(tree) == expected

if __name__ == "__main__":
    main()
