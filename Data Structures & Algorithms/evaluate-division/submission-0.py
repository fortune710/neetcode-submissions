from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for index, (x, y) in enumerate(equations):
            quotient = values[index]
            graph[x].append((y, quotient))
            graph[y].append((x, 1 / quotient))

        def dfs(current: str, target: str, visited: set, product: int):
            if current == target:
                return product

            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited, product * weight)
                    if result != -1:
                        return result

            return -1

        results = []
        for x, y in queries:
            if x not in graph or y not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(x, y, set(), 1.0))

        return results