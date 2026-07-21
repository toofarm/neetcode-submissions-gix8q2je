# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head

        def recurse(slow, fast):
            if fast == None or fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

            return recurse(slow, fast)

        return recurse(slow, fast)