class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, current in enumerate(intervals):

            # Case 1 - new interval is fully before current
            if newInterval[1] < current[0]:
                result.append(newInterval)

                # current and everything after it are already sorted
                return result + intervals[i:]

            # Case 2 - current is fully before new interval
            elif current[1] < newInterval[0]:
                result.append(current)

            # Case 3 - overlap
            else:
                new_start = min(current[0], newInterval[0])
                new_end = max(current[1], newInterval[1])

                # Carry the expanded newInterval forward
                newInterval[0] = new_start
                newInterval[1] = new_end

        # If we reach the end, newInterval still needs to be added
        result.append(newInterval)

        return result