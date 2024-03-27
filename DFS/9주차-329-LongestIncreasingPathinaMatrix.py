class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dxdy = ((1,0), (-1,0), (0,1), (0,-1))
        memo = [[1 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                stack = []
                stack.append((i,j))
                while stack:
                    x, y = stack.pop(-1)
                    for _ in dxdy:
                        nx = x + _[0]; ny = y + _[1]
                        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                            if matrix[nx][ny] > matrix[x][y] and memo[nx][ny] < memo[x][y] + 1:
                                memo[nx][ny] = memo[x][y] + 1
                                stack.append((nx, ny))
        maxi = 0 
        for ___ in memo:
            maxi = max(maxi, max(___))

        return maxi