from collections import deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        
        graph = {i: [] for i in range(n)}
        degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        queue = deque()
        for i in range(n):
            if degree[i] <= 1:
                queue.append(i)
                
        remaining_nodes  = n
        while remaining_nodes > 2:
            size = len(queue)
            remaining_nodes -= size
            
            for _ in range(size):
                node = queue.popleft()
                for neighbor in graph[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                        
        return list(queue)
            