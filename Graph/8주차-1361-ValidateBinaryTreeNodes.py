class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [-1 for _ in range(n)]
        for s in range(n):
            if leftChild[s] != -1:
                if parents[leftChild[s]] != -1:
                    return False
                parents[leftChild[s]] = s 

            if rightChild[s] != -1:
                if parents[rightChild[s]] != -1:
                    return False
                parents[rightChild[s]] = s 


        cnt = 0
        root = -1
        for index, k in enumerate(parents):
            if k == -1:
                root = index
                cnt += 1
        if cnt != 1:
            return False

        visited = []
        queue = [root]
        while queue:
            now = queue.pop(0)
            if now not in visited:
                visited.append(now)
                if leftChild[now] != -1:
                    queue.append(leftChild[now])
                if rightChild[now] != -1:
                    queue.append(rightChild[now])
        if sum(visited) != n*(n-1)//2:
            return False

        return True  