class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        # sort intervals be end time
        intervals.sort(key = lambda x:x[1])        
        # get the first end time
        previous_end = intervals[0][1]

        for current in intervals[1:]:
            # checking if previous end is smaller or equal to the current's start

            if previous_end <= current[0]:
                previous_end = current[1]
            else:
                remove +=1
        return remove
            