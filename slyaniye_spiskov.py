def merger(a, b):
    list_c = []
    n = a + b
    while n:
        num_d = min(n)
        while num_d in n:
            list_c.append(num_d)
            n.remove(num_d)
    return list_c


list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = merger(list_a, list_b)
print(*list_c)
