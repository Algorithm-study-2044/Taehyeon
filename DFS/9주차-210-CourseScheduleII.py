class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        next_steps = [[] for _ in range(numCourses)]
        fore_steps = [[] for _ in range(numCourses)]
        for j in prerequisites:
            next_steps[j[1]].append(j[0])
            fore_steps[j[0]].append(j[1])

        first_nodes = []

        for i, pres in enumerate(fore_steps):
            if not pres:
                first_nodes.append(i)
            
        visited = []
        stack = first_nodes[:]
        path = []

        while stack:
            now = stack.pop(-1)
            if now not in visited:
                path.append(now)
                visited.append(now)
                for _ in next_steps[now]:
                    flag = True
                    for l in fore_steps[_]:
                        if l not in visited:
                            flag = False
                            break
                    if flag:
                        stack.append(_)
        if len(path) != numCourses:
            return []
        else:
            return path
