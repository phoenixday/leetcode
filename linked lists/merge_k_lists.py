class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    head, minn, k = None, 0, -1
    for i, lst in enumerate(lists):
        if lst and (k < 0 or lst.val < minn):
            minn, k = lst.val, i
    if k >= 0:
        head = lists[k]
        lists[k] = lists[k].next
        head.next = merge_k_lists(lists)
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
        [[1,4,5],[1,3,4],[2,6]],
        [],
        [[]]
    ]
    expected = [
        [1,1,2,3,4,4,5,6],
        [],
        []
    ]
    for test, expected in zip(tests, expected):
        l = []
        for t in test:
            l.append(create_linked_list(t))
        assert convert_to_list(merge_k_lists(l)) == expected

if __name__ == "__main__":
    main()
