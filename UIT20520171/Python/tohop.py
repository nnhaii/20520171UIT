import array as Arr
n = int(input())
m = int(input())
result = []
count = 0
Arr[n] = [1]*12
while 0 == 0:
    print(Arr)
    Sum = 0
    for i in range(0, n):
        if Sum >= m:
            break
        Sum += Arr[i]

    if Sum == m and i == n:
        rs = []
        for j in range(0, n):
            rs.append(Arr[j])
        result.append(rs)
    else:
        Arr[i-1] += count
        count += 1
print(result)