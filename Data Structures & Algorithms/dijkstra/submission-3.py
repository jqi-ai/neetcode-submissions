class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        answer = self.init(n, src)
        edgesMap = self.toEdgesMap(edges)
        candidates = [(0, src)]
        heapq.heapify(candidates)
        while candidates:
            curr_distance, curr_node = heapq.heappop(candidates)
            if answer[curr_node] != -1 and curr_distance > answer[curr_node]:
                continue
            neighbors = edgesMap.get(curr_node)
            if neighbors == None:
                continue
            for dest, dist in neighbors.items():
                next_distance = dist + curr_distance
                if answer[dest] == -1 or next_distance < answer[dest]:
                    answer[dest] = next_distance
                    heapq.heappush(candidates, (next_distance, dest))
        return answer
            
    def init(self, n, src):
        answer = dict()
        for i in range(n):
            if i == src:
                answer[i] = 0
            else:
                answer[i] = -1
        return answer

    def toEdgesMap(self, edges):
        m = defaultdict(dict)
        for u, v, w in edges:
            current_w = m.get(u, {}).get(v)
            if current_w and current_w < w:
                continue
            m[u][v] = w
        return m