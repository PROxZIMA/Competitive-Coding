# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head

        for _ in range(n):
            head = head.next

        if head is None:
            return temp.next

        n_from_end = temp

        while head.next:
            head = head.next
            n_from_end = n_from_end.next

        n_from_end.next = n_from_end.next.next
        return temp
