
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjmat = [[] for _ in range(n)]
        for flight in flights:
            adjmat[flight[0]].append((flight[1], flight[2]))
        dist = [9999999 for _ in range(n)]
        dist[src] = 0
        
        queue = [(src, dist[src])]
        steps = 0

        while queue and steps <= k:
            for _ in range(len(queue)):
                now, now_dist = queue.pop(0)

                for next, next_dist in adjmat[now]:
                    if next_dist + now_dist < dist[next]:
                        dist[next] = next_dist + now_dist
                        queue.append((next, dist[next]))
            steps += 1

        return dist[dst] if dist[dst] != 9999999 else -1