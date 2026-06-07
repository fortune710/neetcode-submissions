class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = n
        parents = [i for i in range(n)]

        def find(root):
            while parents[root] != root:
                parents[root] = parents[parents[root]]
                root = parents[root]

            return root

        def union(u, v):
            nonlocal connections
            
            u_root = find(u)
            v_root = find(v)

            if u_root == v_root:
                return u_root

            parents[u_root] = v_root
            connections -= 1

        for u, v in edges:
            union(u, v)

        return connections