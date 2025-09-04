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


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    size, interval = len(lists), 1
    while interval < size:
        for i in range(0, size - interval, interval * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + interval])
        interval *= 2
    return None if size == 0 else lists[0]


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
        [[1,4,5],[1,3,4],[2,6]],
        [],
        [[]],
        [[],[1]],
        [[],[],[],[],[],[],[],[],[],[],[]]
    ]
    expected = [
        [1,1,2,3,4,4,5,6],
        [],
        [],
        [1],
        []
    ]
    for test, expected in zip(tests, expected):
        l = []
        for t in test:
            l.append(create_linked_list(t))
        assert convert_to_list(merge_k_lists(l)) == expected

if __name__ == "__main__":
    main()
