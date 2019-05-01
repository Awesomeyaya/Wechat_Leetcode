# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
时间复杂度 O(len(list)) + O(nk*logk), n is the number of nodes, k is the number of the lists.
空间复杂度 O(k) + O(n) 

min heap里面存的是当前list的第一个元素的值，用于比较， 和当前list的第一个node.
注意每次要判断每一行list是否为空

然后创立一个新的linked list，每次把min-heap中最小的数字加入新的list。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [] 
        for line in lists:
            if line:
                heapq.heappush(heap, (line.val, line)) 
        
        head = tail = ListNode(0)
        while heap:
            curNode = heapq.heappop(heap)[1]
            tail.next = curNode 
            tail = tail.next 
            if curNode.next:
                heapq.heappush(heap, (curNode.next.val, curNode.next))
                
        return head.next
