class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        directs = [[] for __ in range(numCourses)]
        for _ in prerequisites:
            directs[_[1]].append(_[0])
        
        for src in range(numCourses):
            queue = [src]
            visited = []
            while queue:
                now = queue.pop(0)
                if now not in visited:
                    visited.append(now)
                    if src in directs[now]:
                        return False
                    queue.extend(directs[now])
        return True