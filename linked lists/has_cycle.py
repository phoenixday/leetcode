class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def has_cycle(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return False
    if head.val == 100001:
        return True
    head.val = 100001
    return has_cycle(head.next)


# Floyd's Cycle Finding Algorithm
def has_cycle2(head: ListNode | None) -> ListNode | None:
    slower, faster = head, head
    while faster and faster.next and faster.next.next:
        slower, faster = slower.next, faster.next.next
        if slower == faster:
            return True
    return False


# no tests
