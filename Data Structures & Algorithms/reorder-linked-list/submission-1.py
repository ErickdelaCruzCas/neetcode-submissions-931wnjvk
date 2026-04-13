# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, mid = head, head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        
        curr, rev = mid.next, None
        mid.next = None
        while curr:
            tmp = curr.next
            curr.next = rev
            rev = curr
            curr = tmp
        
        first, second = head, rev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2