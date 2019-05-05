这个题目需要选出k个性价比最高的员工。
性价比： wage / quality 

所以，要先把wage/quality从小到大排序，然后用一个priority queue，去求对每一个ratio，最小的工资。
class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        workers = [] 
        for i in range(len(q)):
            workers.append([ float(w[i])/q[i], q[i]])
        workers = sorted(workers, key = lambda x:x[0])
        res, total = float('inf'), 0 
        heap = [] 
        for r, q in workers:
            heapq.heappush(heap, -q)
            total += q 
            if len(heap) > k:
                total += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, r * total)     
        return res
