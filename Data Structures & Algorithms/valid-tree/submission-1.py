class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(len(edges) + 1)]

        def find(root):
            while parent[root] != root:
                parent[root] = parent[parent[root]]
                root = parent[root]

            return root

        def union(u, v):
            u_root = find(u)
            v_root = find(v)

            if u_root == v_root:
                return False

            parent[u_root] = v_root
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True