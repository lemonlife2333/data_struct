#合并两个有序链表

#1.递归
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None :
            return l2
        elif l2 is None :
            return l1
        elif l1.val > l2.val :
            #若l1[0]>l2[0]，则将执行merge(l2[1:],l1),递归化即可
            l2.next = mergeTwoLists(l2.next, l1)
            return l2
        else :
            l1.next = mergeTwoLists(l1.next, l2)
            return l1



#2.迭代
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #构造虚拟头节点
        prehead=ListNode(-1)
        pre=prehead
        
        while l1 and l2 :
            if l1.val <= l2.val : 
                pre.next = l1
                l1 = l1.next
            else :
                pre.next = l2
                l2 = l2.next
            pre = pre.next
            prev.next = l1 if l1 is not None else l2

        return prehead.next
