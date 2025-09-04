import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:
    if node is None:
        return None
    queue = collections.deque([node])
    while queue:
        curr = queue.popleft()
        if curr and curr.val > 0:
            queue.extend(curr.neighbors)
            curr.neighbors.append(Node(curr.val))
            curr.val -= 100
    queue.append(node)
    while queue:
        curr = queue.popleft()
        if curr and curr.val <= 0:
            if curr.neighbors:
                curr_copy = curr.neighbors[-1]
                for neighbor in curr.neighbors:
                    if neighbor.val != curr_copy.val:
                        curr_copy.neighbors.append(neighbor.neighbors[-1])
                        queue.append(neighbor)
            curr.val += 100
    root = node.neighbors[-1]
    queue.append(node)
    while queue:
        curr = queue.popleft()
        if curr and curr.val > 0:
            if curr.neighbors:
                curr.neighbors.pop()
                queue.extend(curr.neighbors)
            curr.val -= 100
    queue.append(node)
    while queue:
        curr = queue.popleft()
        if curr and curr.val <= 0:
            if curr.neighbors:
                queue.extend(curr.neighbors)
            curr.val += 100
    return root


def clone_graph_with_set(node: Node | None) -> Node | None:
    if node is None:
        return None
    queue = collections.deque([node])
    nodes_seen: set[int] = set()
    while queue:
        curr = queue.popleft()
        if curr and curr.val not in nodes_seen:
            queue.extend(curr.neighbors)
            curr.neighbors.append(Node(curr.val))
            nodes_seen.add(curr.val)
    nodes_seen: set[int] = set()
    queue.append(node)
    while queue:
        curr = queue.popleft()
        if curr and curr.neighbors and curr.val not in nodes_seen:
            curr_copy = curr.neighbors[-1]
            for neighbor in curr.neighbors:
                if neighbor.val != curr_copy.val:
                    curr_copy.neighbors.append(neighbor.neighbors[-1])
                    queue.append(neighbor)
            nodes_seen.add(curr.val)
    root = node.neighbors[-1]
    nodes_seen: set[int] = set()
    queue.append(node)
    while queue:
        curr = queue.popleft()
        if curr and curr.neighbors and curr.val not in nodes_seen:
            curr.neighbors.pop()
            queue.extend(curr.neighbors)
            nodes_seen.add(curr.val)
    return root


def clone_graph_dfs(node: Node | None, visited: dict[int, Node] = None) -> Node | None:
    if node is None:
        return None
    if visited is None:
        visited = {}
    if node.val in visited:
        return visited[node.val]
    new_node = Node(node.val)
    visited[node.val] = new_node
    new_node.neighbors = [clone_graph_dfs(n, visited) for n in node.neighbors]
    return new_node


def clone_graph_bfs(node: Node | None) -> Node | None:
    if node is None:
        return None
    visited: dict[int, Node] = {node.val: Node(node.val)}
    queue = collections.deque([node])
    while queue:
        curr = queue.pop()
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = Node(neighbor.val)
                queue.append(neighbor)
            visited[curr.val].neighbors.append(visited[neighbor.val])
    return visited[node.val]


def get_or_create(nodes_seen: dict[int, Node], num: int) -> Node:
    if num not in nodes_seen:
        nodes_seen[num] = Node(num)
    return nodes_seen[num]


def create_graph(lst: list[list[int]])  -> Node | None:
    if len(lst) == 0:
        return None
    nodes_seen: dict[int, Node] = {}
    for i, neighbors in enumerate(lst):
        node = get_or_create(nodes_seen, i + 1)
        for n in neighbors:
            neighbor = get_or_create(nodes_seen, n)
            node.neighbors.append(neighbor)
    return nodes_seen[1]


def check_graph(graph: Node | None, lst: list[list[int]]) -> bool:
    if graph is None:
        return len(lst) == 0
    vals_seen = set()
    queue = collections.deque([graph])
    while queue:
        node = queue.popleft()
        if len(lst) <= node.val - 1:
            return False
        if len(lst[node.val - 1]) != len(node.neighbors):
            return False
        for i, n in enumerate(lst[node.val - 1]):
            if n != node.neighbors[i].val:
                return False
            if n not in vals_seen:
                queue.append(node.neighbors[i])
                vals_seen.add(n)
    return True


def main():
    tests = [
        [[2,4],[1,3],[2,4],[1,3]],
        [[]],
        []
    ]
    for test in tests:
        graph = create_graph(test)
        cloned_graph = clone_graph_bfs(graph)
        assert check_graph(cloned_graph, test)


if __name__ == "__main__":
    main()
