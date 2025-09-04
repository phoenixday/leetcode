class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def get_number(lst: ListNode | None) -> int:
    summ = lst.val
    while lst.next:
        lst = lst.next
        summ = summ * 10 + lst.val
    return summ


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    summ = get_number(l1) + get_number(l2)
    head, prev = ListNode(), None
    while summ > 0:
        head = ListNode(summ % 10)
        head.next = prev
        prev = head
        summ //= 10
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
