class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Node | None) -> Node | None:
    pairs: dict[Node, Node | None] = {}
    curr, curr_new, prev, new_head = head, None, None, None
    while curr:
        curr_new = Node(curr.val)
        if not new_head:
            new_head = curr_new
        if prev:
            prev.next = curr_new
        pairs[curr] = curr_new
        prev = curr_new
        curr = curr.next
    for old, new in pairs.items():
        random: Node | None = old.random
        if random:
            new.random = pairs[random]
    return new_head


def copy_random_list2(head: Node | None) -> Node | None:
    if not head:
        return None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = Node(curr.val, next=nxt, random=curr.random)
        curr = nxt
    curr = head.next
    while curr:
        if curr.random:
            curr.random = curr.random.next
        curr = None if not curr.next else curr.next.next
    curr, head_new = head, head.next
    while curr and curr.next:
        copied = curr.next
        curr.next = copied.next
        if copied.next:
            copied.next = copied.next.next
        curr = curr.next
    return head_new


def copy_random_list3(head: Node | None, pairs: dict[Node, Node | None] = None) -> Node | None:
    if not head:
        return None
    if not pairs:
        pairs = {}
    if head in pairs:
        return pairs[head]
    node = Node(head.val)
    pairs[head] = node
    node.next = copy_random_list3(head.next, pairs)
    node.random = copy_random_list3(head.random, pairs)
    return node


def copy_random_list4(head: Node | None) -> Node | None:
    pairs: dict[Node, Node | None] = {}
    curr, head_new = head, None
    while curr:
        if curr in pairs:
            node = pairs[curr]
        else:
            node = Node(curr.val)
            pairs[curr] = node
        if curr.next and not node.next:
            if curr.next in pairs:
                node.next = pairs[curr.next]
            else:
                node.next = Node(curr.next.val)
                pairs[curr.next] = node.next
        if curr.random and not node.random:
            if curr.random in pairs:
                node.random = pairs[curr.random]
            else:
                node.random = Node(curr.random.val)
                pairs[curr.random] = node.random
        if not head_new:
            head_new = node
        curr = curr.next
    return head_new




# no tests
