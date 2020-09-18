class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.adj_list = defaultdict(list)
        self.seen = set()
        self.nodes_ids = {}
        self.min_nodes_ids = {}
        self.to_return = []
        self.cur_id = -1
        for connection in connections:
            self.adj_list[connection[0]].append(connection[1])
            self.adj_list[connection[1]].append(connection[0])
        def dfs(prev, node):
            self.cur_id+=1
            self.seen.add(node)
            self.nodes_ids[node] = self.cur_id
            self.min_nodes_ids[node] = self.cur_id
            for neighbor in self.adj_list[node]:
                if neighbor == prev:
                    continue
                if neighbor in self.seen:
                    self.min_nodes_ids[node] = min(self.min_nodes_ids[node], self.min_nodes_ids[neighbor])
                else:
                    neighbor_min_id = dfs(node, neighbor)
                    self.min_nodes_ids[node] = min(self.min_nodes_ids[node], neighbor_min_id)
                    if self.nodes_ids[node] < neighbor_min_id:
                        self.to_return.append([node, neighbor])
            return self.min_nodes_ids[node]
        dfs(None, 0)
        print(self.nodes_ids)
        return self.to_return