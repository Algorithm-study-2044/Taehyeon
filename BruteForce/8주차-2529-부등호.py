def make_number(index, length):
    num = ''
    temp = [0 for _ in range(length)]
    for nume, ord in enumerate(index):
        if ord != -1:
            temp[ord] = nume 
    for _ in temp:
        num = num + str(_) 
    return int(num)

k = int(input())
ineqs = list(input().split())
minn = 99999999999999
maxn = 0

index = [-1 for _ in range(10)]

def find_next(order, cur):
    global index, minn, maxn
    if order == k:
        result = make_number(index, k+1)
        minn = min(minn, result)
        maxn = max(maxn, result)
        return
    
    for next in range(10):
        if index[next] == -1:
            if ineqs[order] == '<':
                if next > cur:
                    index[next] = index[cur] + 1
                    find_next(order+1, next)
                    index[next] = -1
            else:
                if cur > next:
                    index[next] = index[cur] + 1
                    find_next(order+1, next)
                    index[next] = -1
    return

for i in range(10):
    index[i] = 0
    find_next(0, i)
    index[i] = -1
maxn = str(maxn)
if minn < 10**k:
    minn = '0' + str(minn)
else:
    minn = str(minn)

print(maxn)
print(minn)



