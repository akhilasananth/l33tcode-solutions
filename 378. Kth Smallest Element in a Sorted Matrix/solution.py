from heapq import heapify, heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ret_val = 0

        heap = []
        heapify(heap)

        for row in matrix:
            for num in row:
                heappush(heap, num)

        for n in range(1, k + 1):
            ret_val = heappop(heap)

        return ret_val