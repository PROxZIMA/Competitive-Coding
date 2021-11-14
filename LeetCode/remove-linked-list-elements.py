# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        tail = temp
        while tail.next:
            if tail.next.val == val:
                tail.next = tail.next.next
            else:
                tail = tail.next
        return temp.next
