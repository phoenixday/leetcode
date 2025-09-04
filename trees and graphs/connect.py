import collections

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next_node: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_node


def connect(root: Node | None) -> Node | None:
    queue = collections.deque([root])
    while queue:
        length = len(queue)
        for i in range(length):
            node = queue.popleft()
            if node:
                if i < length - 1:
                    node.next = queue[0]
                queue.append(node.left)
                queue.append(node.right)
    return root


def connect_with_list(root: Node | None) -> Node | None:
    queue, i = [root], 0
    while i < len(queue):
        level_len = len(queue) - i
        for j in range(level_len):
            node = queue[i + j]
            if node:
                if j < level_len - 1:
                    node.next = queue[i + j + 1]
                queue.append(node.left)
                queue.append(node.right)
        i += level_len
    return root


def connect_without_queue(root: Node | None) -> Node | None:
    level_first = root
    # we're moving between levels by left nodes from current node
    while level_first and level_first.left:
        curr = level_first
        while curr:
            if curr.left:
                curr.left.next = curr.right
            if curr.right and curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        level_first = level_first.left
    return root


def convert_to_tree_node(lst: list[int | None], i=0) -> Node | None:
    if len(lst) <= i or not lst[i]:
        return None
    return Node(lst[i],
                    convert_to_tree_node(lst, i * 2 + 1),
                    convert_to_tree_node(lst, i * 2 + 2))


def main():
    tests = [
        [1, 2, 3, 4, 5, 6, 7],
        []
    ]
    expected = [
        [1, 2, 3, 4, 5, 6, 7],
        []
    ]
    for test, expected in zip(tests, expected):
        assert connect_without_queue(convert_to_tree_node(test)) == expected

if __name__ == "__main__":
    main()
