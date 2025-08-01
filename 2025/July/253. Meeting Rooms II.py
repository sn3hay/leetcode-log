class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ending_times = []
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        prev_end = intervals[0][1]
        count = 1
        ending_times.append(prev_end)
        for curr_start, curr_end in intervals[1:]:
            if curr_start < prev_end:
                ending_times.append(curr_end)
            else:
                # it goes in the same room, so update its ending time 
                index = ending_times.index(prev_end)
                ending_times[index] = curr_end
            prev_end = min(ending_times)
        
        min_heap =[]
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, intervals[0][1])
        for curr_start, curr_end in intervals[1:]:
            if curr_start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, curr_end)
            
        return len(min_heap)
        
