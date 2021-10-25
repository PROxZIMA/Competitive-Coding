# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        bitSum, c = 0, 0
        head = ListNode()
        h = head

        while c or l1 or l2:
            if l1:
                bitSum += l1.val
                l1 = l1.next
            if l2:
                bitSum += l2.val
                l2 = l2.next

            bitSum += c
            c = bitSum // 10
            head.next = ListNode(bitSum % 10)
            head = head.next
            bitSum = 0

        return h.next
