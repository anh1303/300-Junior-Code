from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        answer = 0
        
        while queue:
            size = len(queue)
            
            first_index = queue[0][1]
            last_index = first_index
            
            for _ in range(size):
                node, index = queue.popleft()
                last_index = index
                
                if node.left:
                    queue.append((node.left, 2 * index))
                    
                if node.right:
                    queue.append((node.right, 2*index + 1))
                    
            answer = max(answer, last_index - first_index + 1)
            
        return answer