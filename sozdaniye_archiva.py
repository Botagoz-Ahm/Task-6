s, n = map(int, input().split())
obiem = sorted([int(input()) for i in range(n)])
kolvo = sum(obiem)
while kolvo > s and n:
    kolvo = kolvo - obiem.pop()
    n = n - 1
print(n)
