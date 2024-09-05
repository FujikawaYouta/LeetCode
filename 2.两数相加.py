# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 链表练习
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root_node = ListNode()
        l_ans = root_node
        c = 0
        while l1!=None or l2!=None or c!=0:
            val1 = l1.val if l1!=None else 0
            val2 = l2.val if l2!=None else 0
            l_ans.val=(val1+val2+c)%10
            c=(val1+val2+c)//10
            l1 = l1.next if l1!=None else None
            l2 = l2.next if l2!=None else None
            if l1!=None or l2!=None or c!=0:
                l_ans.next = ListNode()
            else:
                break
            l_ans = l_ans.next
        return root_node

def generateListNode(nums: list)-> ListNode:
    n = len(nums)
    root_node = ListNode()
    cur_node = root_node
    for i,num in enumerate(nums):
        cur_node.val=num
        if i==n-1:
            break
        cur_node.next=ListNode()
        cur_node=cur_node.next
    return root_node

if __name__ == '__main__':
    l1 = generateListNode([9,9,9,9,9,9,9,9,9])
    l2 = generateListNode([9,9,9,9])
    sol = Solution()
    print(sol.addTwoNumbers(l1,l2))