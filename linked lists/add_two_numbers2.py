class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def get_length(lst: ListNode | None) -> int:
    if not lst:
        return 0
    return 1 + get_length(lst.next)


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    summ = 0
    l1_length = get_length(l1)
    l2_length = get_length(l2)
    while l1_length > 0:
        if l1_length > l2_length:
            summ += l1.val * pow(10, l1_length - 1)
            l1_length -= 1
            l1 = l1.next
        elif l2_length > l1_length:
            summ += l2.val * pow(10, l2_length - 1)
            l2_length -= 1
            l2 = l2.next
        else:
            summ += (l1.val + l2.val) * pow(10, l1_length - 1)
            l1_length -= 1
            l2_length -= 1
            l1 = l1.next
            l2 = l2.next
    max_len, d = 1, 10
    while summ // d > 0:
        max_len += 1
        d = pow(10, max_len)
    head, prev = None, None
    for d in range(max_len, 0, -1):
        dec = pow(10, d - 1)
        l = ListNode(summ // dec)
        summ = summ % dec
        if d == max_len:
            head = l
        if prev:
            prev.next = l
        prev = l
        l = l.next
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
