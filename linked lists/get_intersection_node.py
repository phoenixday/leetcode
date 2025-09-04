from collections import deque

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode | None:
    maxx = 100000
    a = headA
    while a:
        a.val -= maxx
        a = a.next
    b, res = headB, None
    while b:
        if b.val <= 0:
            res = b
            break
        b = b.next
    a = headA
    while a:
        a.val += maxx
        a = a.next
    return res


def get_intersection_node2(headA: ListNode, headB: ListNode) -> ListNode | None:
    maxx = 100000
    a, b, res = headA, headB, None
    while a or b:
        if a == b or (a and a.val <= 0) or (b and b.val <= 0):
            res = a if (a and a.val <= 0) else b
            break
        if a:
            a.val -= maxx
            a = a.next
        if b:
            b.val -= maxx
            b = b.next
    a = headA
    while a and a.val <= 0:
        a.val += maxx
        a = a.next
    b = headB
    while b and b.val <= 0:
        b.val += maxx
        b = b.next
    return res


def get_length(head: ListNode) -> int:
    length, p = 0, head
    while p:
        length += 1
        p = p.next
    return length


def get_intersection_node3(headA: ListNode, headB: ListNode) -> ListNode | None:
    a_len, b_len = get_length(headA), get_length(headB)
    a, b = headA, headB
    while a and b:
        if a_len > b_len:
            a = a.next
            a_len -= 1
        elif b_len > a_len:
            b = b.next
            b_len -= 1
        else:
            if a == b:
                return a
            a = a.next
            b = b.next
    return None


def get_intersection_node4(headA: ListNode, headB: ListNode) -> ListNode | None:
    pA = headA
    pB = headB
    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    return pA


# no tests
