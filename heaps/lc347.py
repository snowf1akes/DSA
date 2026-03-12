#Top K frequent Elements

#neetcode version --> using bucketsort but tweaked
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #index of array
        freq = [[] for i in range(len(nums)+ 1)]#value list

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

#min heaps version nlogk

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [h[1] for h in heap]
    
#max heaps --> o(n) answer

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        res = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                res.extend(buckets[i])
            if len(res) == k:
                break

        return res

#basic OA version

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq. heappushpop(heap, (val, key))
        
        res = []
        for h in heap:
            res.append(h[1])
        return res

