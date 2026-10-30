class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the list of empty lists and this list will hold prequisite course for each course

        graph = [[] for course in range(numCourses)]
        # setting prerequisite of each course as 0 first
        indegree = [0] * numCourses

        # build graph , here we hav course as vertices (nodes) and prequisites as edges (connection between nodes)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque()

        # add all the course to queue that can be started, meaning has no preq (indegree == 0)

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0
        while queue:
            # get the first course with zero prequisite from queue
            course = queue.popleft()
            completed += 1
            # this course is now completed so all the course that depends on it can be taken and their indegree should be reduce by one
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        if completed == numCourses:
            return True
        else:
            return False
