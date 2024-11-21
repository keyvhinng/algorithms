from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer_query(start, end):
            if start not in graph:
                return -1
            
            seen = {start}
            stack = [(start,1)]

            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, ratio*graph[node][neighbor]))
            return -1

        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator, denomitator = equations[i]
            val = values[i]
            graph[numerator][denomitator] = val
            graph[denomitator][numerator] = 1 / val

        ans = []
        for numerator, denomitator in queries:
            ans.append(answer_query(numerator, denomitator))

        return ans
