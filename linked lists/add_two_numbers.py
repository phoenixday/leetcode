class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def add_two_numbers(l1: ListNode | None, l2: ListNode | None, carry: int = 0) -> ListNode | None:
    if not l1 and not l2:
        if carry > 0:
            return ListNode(carry)
        return None
    v1 = 0 if not l1 else l1.val
    v2 = 0 if not l2 else l2.val
    node = ListNode((v1 + v2 + carry) % 10)
    carry = (v1 + v2 + carry) // 10
    node.next = add_two_numbers(None if not l1 else l1.next, None if not l2 else l2.next, carry)
    return node


def create_linked_list(lst: list[int], i=0) -> ListNode | None:
    if len(lst) <= i:
        return None
    return ListNode(val=lst[i], next_node=create_linked_list(lst, i + 1))


def convert_to_list(head: ListNode | None) -> list[int]:
    res = []
    cur = head
    while cur is not None:
        res.append(cur.val)
        cur = cur.next
    return res


def main():
    tests = [
        ([2,4,3], [5,6,4]),
        ([0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9])
    ]
    expected = [
        [7,0,8],
        [0],
        [8,9,9,9,0,0,0,1]
    ]
    for test, expected in zip(tests, expected):
        ll1, ll2 = test
        l1, l2 = create_linked_list(ll1), create_linked_list(ll2)
        assert convert_to_list(add_two_numbers(l1, l2)) == expected

if __name__ == "__main__":
    main()
