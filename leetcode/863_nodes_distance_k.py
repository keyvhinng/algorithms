from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k:int) -> list[int]:
        def dfs(node, parent):
            if not node:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        queue = deque([target])
        seen = {target}
        distance = 0

        while queue and distance < k:
            current_length = len(queue)
            for _ in range(current_length):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1

        return [node.val for node in queue]
