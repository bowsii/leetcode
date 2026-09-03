class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:
        def dfs(node):
            if node == dest:
                return True
            if node in visited:
                return False
            visited.add(node)
            for i in gh[node]:
                if dfs(i):
                    return True
            return False

        
        gh = [[] for _ in range(n)]
        
        for u,v in edges:
            gh[u].append(v)
            gh[v].append(u)
        visited = set()
        return dfs(src)