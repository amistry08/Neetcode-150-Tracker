class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for i in stones:
            heapq.heappush(minHeap, i *-1)
        while len(minHeap) >= 2:
            y = -1 * heapq.heappop(minHeap)
            x = -1 * heapq.heappop(minHeap)
            if x != y:
                heapq.heappush(minHeap, x-y)
        
        return -minHeap[0] if len(minHeap) == 1 else  0