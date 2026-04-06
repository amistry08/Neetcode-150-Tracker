
import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        
        if len(self.maxHeap) > 0 and num < self.maxHeap[0]:
            heapq.heappush(self.minHeap, -1 * num)
        else:
            heapq.heappush(self.maxHeap, num)

        while abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                n = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap,-1 * n)
            else:
                n = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * n)


    def findMedian(self) -> float:
        print(len(self.maxHeap) , len(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap):
            return -1 * self.minHeap[0]
        else:
            return ((-1 * self.minHeap[0]) + self.maxHeap[0]) / 2