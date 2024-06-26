# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        merged = dummy
        l1 = list1
        l2 = list2

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next

        # Append the remaining elements
        if l1 is not None:
            merged.next = l1
        else:
            merged.next = l2

        return dummy.next