from typing import List

class Solution:
    def allPathsSourceTarget(self, graph:List[List[int]]) -> List[List[int]]:
        ans = []

        def dfs(node, path):
            if node == n-1:
                ans.append(path[:])

            for v in graph[node]:
                path.append(v)
                dfs(v, path)
                path.pop()


        n = len(graph)
        dfs(0,[0]);


        return ans
