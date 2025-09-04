class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def reverse_list_iter(head: ListNode | None) -> ListNode | None:
    curr, prev = head, None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


#  val 1 2 3 4 5
#  nxt 2 3 4 5 -

#  val 1 2 3 4 5
#  nxt - 1 2 3 4

def reverse_list_rec(head: ListNode | None, prev: ListNode | None = None) -> ListNode | None:
    if head is None:
        return None
    nxt = head.next
    head.next = prev
    if nxt is None:
        return head
    return reverse_list_rec(nxt, head)


def reverse_list_rec2(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    last = reverse_list_rec2(head.next)
    head.next.next = head
    head.next = None
    return last


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
        [1,2,3,4,5],
        [1,2],
        [1],
        []
    ]
    expected = [
        [5,4,3,2,1],
        [2,1],
        [1],
        []
    ]
    for test, expected in zip(tests, expected):
        assert convert_to_list(reverse_list_rec2(create_linked_list(test))) == expected

if __name__ == "__main__":
    main()
