class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for x in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, x)
            else:
                if x > minHeap[0]:
                    heapq.heapreplace(minHeap, x)
        return minHeap[0]