# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return

        if list1 is None:
            new_head = list2
            new_list1 = None
            new_list2 = list2.next
        elif list2 is None:
            new_head = list1
            new_list2 = None
            new_list1 = list1.next
        else:
            new_head = list1 if list1.val <= list2.val else list2
            new_list1 = list1.next if list1.val <= list2.val else list1
            new_list2 = list2.next if list1.val > list2.val else list2

        def recurse(l1: Optional[ListNode], 
            l2: Optional[ListNode],
            acc: Optional[ListNode]) -> Optional[ListNode]:
            if l1:
                print(f"l1 val: {l1.val}")
            if l2:
                print(f"l2 val: {l2.val}")

            if l1 == None and l2 == None:
                return

            if l1 is None:
                acc.next = l2
                return recurse(l1, l2.next, acc.next)
            elif l2 is None:
                acc.next = l1
                return recurse(l1.next, l2, acc.next)
            else:
                next_node = l1 if l1.val <= l2.val else l2
                acc.next = next_node
                print(f"next_node val: {next_node.val}")
                return recurse(l1.next if l1.val <= l2.val else l1, 
                    l2.next if l2.val < l1.val else l2, 
                    acc.next)

        recurse(new_list1, 
            new_list2, 
            new_head)

        return new_head


