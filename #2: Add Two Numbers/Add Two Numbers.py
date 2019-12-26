# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        head = ListNode(0)
        cur = head
        while (l1 or l2 or carry):
            tmp = carry
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            cur.next = ListNode(tmp % 10)
            carry = tmp // 10
            cur = cur.next
        return head.next