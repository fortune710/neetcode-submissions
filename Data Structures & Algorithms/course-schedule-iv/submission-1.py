from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)

        for prerequisite, course in prerequisites:
            graph[course].add(prerequisite)

        def dfs(current: int, target: int, visited: set) -> bool:

            if current == target:
                return True

            visited.add(current)
            base_prerequisites = graph.get(current, None)
            if not base_prerequisites:
                return False

            for prerequisite in base_prerequisites:
                if prerequisite in visited:
                    continue
                    
                is_prerequisite = dfs(prerequisite, target, visited)
                if is_prerequisite is not False:
                    return is_prerequisite

            return False

        results = []
        for prerequisite, course in queries:
            results.append(dfs(course, prerequisite, set()))

        return results