class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculate(x, y):
            return math.sqrt( (x * x) + (y * y) ) 
        
        minHeap = []
        for i in points:
            minHeap.append([calculate(i[0], i[1]), i])
        
        heapq.heapify(minHeap)
        
        res = []
        for i in range(k):
            x = heapq.heappop(minHeap)
            res.append(x[1])

        return res