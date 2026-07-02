"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        visited = {}
        
        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            new_node = Node(curr_node.val)
            visited[curr_node] = new_node
            for neighbor in curr_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)