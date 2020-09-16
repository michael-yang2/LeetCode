class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def recur(node, visited):
            if node in self.checked:
                return True
            if node in visited:
                return False
            to_ret = True
            visited.add(node)
            for adj in self.adj_list[node]:
                to_ret = to_ret and recur(adj, visited)
            visited.remove(node)
            self.checked.add(node)
            return to_ret
        self.adj_list = [[] for i in range(numCourses)]
        self.checked = set()
        for course, prereq in prerequisites:
            self.adj_list[prereq].append(course)
        for i in range(len(self.adj_list)):
            if not recur(i, set()):
                return False
        return True