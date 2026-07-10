class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        
        num_prereq_left = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            num_prereq_left[course] += 1
            
        queue = [i for i in range(numCourses) if num_prereq_left[i] == 0]
        
        count = 0
        while queue:
            prereq = queue.pop(0)
            count += 1
            
            for course in graph[prereq]:
                num_prereq_left[course] -= 1
                if num_prereq_left[course] == 0:
                    queue.append(course)

        return count == numCourses