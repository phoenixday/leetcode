class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if not list1:
        return list2
    if not list2:
        return list1
    head, curr, prev = None, None, None
    while list1 and list2:
        if list1.val <= list2.val:
            curr = list1
            list1 = list1.next
        else:
            curr = list2
            list2 = list2.next
        if prev:
            prev.next = curr
        if not head:
            head = curr
        prev = curr
    if list1:
        prev.next = list1
    if list2:
        prev.next = list2
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
        ([1,2,4], [1,3,4]),
        ([], []),
        ([], [0])
    ]
    expected = [
        [1,1,2,3,4,4],
        [],
        [0]
    ]
    for test, expected in zip(tests, expected):
        ll1, ll2 = test
        l1, l2 = create_linked_list(ll1), create_linked_list(ll2)
        assert convert_to_list(merge_two_lists(l1, l2)) == expected

if __name__ == "__main__":
    main()
