class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 10**10
        adj = defaultdict(list)
        dist = [INF]*n
        for edge in times:
            adj[edge[0] - 1].append([edge[1] - 1, edge[2]])
        def dijkstra():
            nonlocal dist
            dist[k - 1] = 0

            pq = [[0, k - 1]]
            while pq:
                d, u = heapq.heappop(pq)
                for v, wt in adj[u]:
                    if dist[v] > dist[u] + wt:
                        dist[v] = dist[u] + wt
                        heapq.heappush(pq, [dist[v], v])

        dijkstra()
        ans = -1
        for i in range(n):
            if dist[i] == INF:
                return -1
            ans = max(ans, dist[i])
        return ans
