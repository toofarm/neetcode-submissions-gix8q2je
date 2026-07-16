# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        def recurse(head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            next = head.next
            head.next = prev

            if not next:
                return head
            else:
                return recurse(next, head)

        return recurse(head, None)
