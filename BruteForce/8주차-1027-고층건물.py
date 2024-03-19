N = int(input())
heights = list(map(int, input().split()))
ans = 0
for i in range(N):
    seeing = 0
    for j in range(N):
        if i == j:
            continue
        flag = True
        for b in range(min(i,j)+1, max(i,j)):
            if heights[i] <= heights[j]:
                if heights[b] >= heights[i] + (heights[j]-heights[i])*abs(b-i)/abs(j-i):
                    flag = False
            else:
                if heights[b] >= heights[j] + (heights[i]-heights[j])*abs(j-b)/abs(j-i):
                    flag = False
        if flag:
            seeing += 1
    ans = max(ans, seeing)
print(ans)