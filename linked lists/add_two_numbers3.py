from collections import deque


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def create_deque(lst: ListNode | None):
    d = deque()
    while lst:
        d.append(lst.val)
        lst = lst.next
    return d


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    d1 = create_deque(l1)
    d2 = create_deque(l2)
    head, prev, carry = None, None, 0
    while d1 or d2 or carry > 0:
        summ = carry
        if d1:
            summ += d1.pop()
        if d2:
            summ += d2.pop()
        carry = summ // 10
        head = ListNode(summ % 10)
        head.next = prev
        prev = head
    return head


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
        ([7,2,4,3], [5,6,4]),
        ([0], [0]),
        ([1,0,0], [0]),
        ([2,4,3], [5,6,4]),
        ([5], [5]),
        ([0], [1]),
        ([1], [0])
    ]
    expected = [
        [7,8,0,7],
        [0],
        [1,0,0],
        [8,0,7],
        [1,0],
        [1],
        [1]
    ]
    for test, expected in zip(tests, expected):
        ll1, ll2 = test
        l1, l2 = create_linked_list(ll1), create_linked_list(ll2)
        assert convert_to_list(add_two_numbers(l1, l2)) == expected

if __name__ == "__main__":
    main()
