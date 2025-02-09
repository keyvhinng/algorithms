from typing import List

class Solution:
    """
        States:
        0 -> unvisited
        1 -> visiting
        2 -> safe
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = {}
        n = len(graph)

        def is_safe(index):
            if state.get(index) == 1:
                return False

            if graph[index] == []:
                state[index] = 2
                return True

            if graph[index] == 2:
                return True

            state[index] = 1

            for v in graph[index]:
                if not is_safe(v):
                    return False

            state[index] = 2
            return True

        result = []

        for i in range(n):
            if is_safe(i):
                result.append(i)

        return result

