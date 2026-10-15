class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
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

        
