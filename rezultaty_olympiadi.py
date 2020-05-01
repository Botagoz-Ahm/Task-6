n = int(input())
lists = [input().split() for i in range(n)]
for i in sorted(lists, key=lambda x: int(x[1]), reverse=True):
    print(i[0])
