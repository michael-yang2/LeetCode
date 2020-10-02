class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for edge in red_edges:
            adj_list[edge[0]].append([0, edge[1]])#0 = red, 1 = blue
        for edge in blue_edges:
            adj_list[edge[0]].append([1, edge[1]])
        to_return = [sys.maxsize]*n
        nodes = deque()
        nodes.append((0,0,0))
        nodes.append((0,1,0))
        visited = set()
        while nodes:
            node, node_color,pathlength = nodes.popleft()
            if (node, node_color) in visited:
                continue
            visited.add((node, node_color))
            to_return[node] = min(to_return[node], pathlength)
            for neighbor_color, neighbor in adj_list[node]:
                if neighbor_color == (node_color+1)%2:
                    nodes.append((neighbor, neighbor_color,pathlength+1))
        for i in range(len(to_return)):
            if to_return[i] == sys.maxsize:
                to_return[i] = -1
        return to_return
                    