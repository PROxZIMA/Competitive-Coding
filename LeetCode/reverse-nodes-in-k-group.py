# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse first k nodes and return if k == length(list)
        prev, curr, _ = self.reverse(head, k)
        sol = prev

        if not curr:
            return sol

        # reverse k nodes until list ends
        while curr:
            head2 = curr
            prev, curr, i = self.reverse(curr, k)
            head.next = prev
            prevHead = head
            head = head2

        # again reverse last length(list) - k nodes
        if i < k:
            prev, curr, _ = self.reverse(prev, k)
            prevHead.next = prev
        return sol

    def reverse(self, head: Optional[ListNode], k: int) -> (Optional[ListNode], Optional[ListNode], int):
        i = 0
        prev = None
        curr = head
        while curr and i < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        return prev, curr, i

