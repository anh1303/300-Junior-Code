class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = {i: [] for i in range(numCourses)}
        degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            degree[course] += 1
            
        order = []
        queue = [i for i in range(numCourses) if degree[i] == 0]
        
        while queue:
            course = queue.pop(0)
            order.append(course)
            
            for neighbor in graph[course]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return order if len(order) == numCourses else []