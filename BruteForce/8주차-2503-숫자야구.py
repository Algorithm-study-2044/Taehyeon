def check(ans, trial):
    ball = 0
    strike = 0
    for i in range(3):
        if ans[i] == trial[i]:
            strike += 1
    for i in range(3):
        for j in range(3):
            if i == j:
                continue 
            if ans[i] == trial[j]:
                ball += 1
    return [strike, ball]


candid = []
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == j or k == i:
                continue 
            candid.append(str(100*i+10*j+k))
N = int(input())
quests = []
for _ in range(N):
    a, b, c = input().split()
    quests.append([a,int(b),int(c)])

new_candid = candid[:]
for e in quests:
    for r in new_candid:
        if (check(r, e[0])[0] == e[1]) and (check(r, e[0])[1] == e[2]):
            continue
        if r in candid:
            candid.remove(r)
print(len(candid))