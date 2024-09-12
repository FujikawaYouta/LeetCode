# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        fast = fast.next
        cur_sum = 0
        while fast:
            if fast.val == 0:
                slow.next.val = cur_sum
                slow = slow.next
                cur_sum = 0
            else:
                cur_sum += fast.val
            fast = fast.next
        slow.next = None
        return head.next

def generateListNode(nums: list) -> Optional[ListNode]:
    n = len(nums)
    root = ListNode()
    cur_root = root
    for i,num in enumerate(nums):
        cur_root.val = num
        if i==n-1:
            break
        cur_root.next = ListNode()
        cur_root = cur_root.next
    return root
     
if __name__ == '__main__':
    sol = Solution()
    head = generateListNode(nums = [0,3,1,0,4,5,2,0])
    print(sol.mergeNodes(head))