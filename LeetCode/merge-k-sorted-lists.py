# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lenList = len(lists)
        if lenList == 0:
            return
        if lenList == 1:
            if lists[0]:
                return lists[0]
            else:
                return
        de = deque(lists)
        while len(de) > 1:
            A = de.popleft()
            B = de.popleft()
            de.append(self.merge2list(A, B))

        return de[0]

    def merge2list(self, A: ListNode, B: ListNode) -> ListNode:
        if not(A or B): return
        if not(A and B): return A or B
        
        if (A.val < B.val):
            head = A
            head.next = self.merge2list(A.next, B)
        else:
            head = B
            head.next = self.merge2list(A, B.next)
        
        return head

    # naive merge one by one
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lenList = len(lists)
        if lenList == 0:
            return
        if lenList == 1:
            if lists[0]:
                return lists[0]
            else:
                return
            
        A = lists[0]
        
        for i in range(1, lenList):
            B = lists[i]
            dummy = ListNode()

            tail = dummy
            while True:
                if not(A and B):
                    tail.next = A or B
                    break

                if A.val <= B.val:
                    tail.next = A
                    A = A.next
                else:
                    tail.next = B
                    B = B.next

                tail = tail.next

            A = dummy.next
        
        return A


