class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # storing coming values to a dict and then list of tuples
        # check if dict is empty ,  first call
        if key not in self.store:
            self.store[key] = []
        #appending a key's value to its list
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        # doing binray search on the list of key
        space = self.store[key]
        left = 0
        right = len(space) - 1

        answer = ""

        while left <= right:
            mid = (left + right) // 2

            if space[mid][0] <= timestamp:
                answer = space[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return answer

        
