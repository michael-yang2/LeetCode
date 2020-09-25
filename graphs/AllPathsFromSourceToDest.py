class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        node_map = {}
        seen = set()
        for start, end in edges:
            adj_list[start].append(end)
        def dfs(src, dest):
            if src == dest:
                return True
            if len(adj_list[src]) == 0:
                return False
            if src in seen:
                return False
            if src in node_map:
                return node_map[src]
            seen.add(src)
            to_return = True
            for node in adj_list[src]:
                to_return = to_return and dfs(node, dest)
            node_map[src] = to_return
            seen.remove(src)
            return to_return
        if len(adj_list[destination]) != 0:
            return False
        return dfs(source, destination)