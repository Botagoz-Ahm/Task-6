def CountSort(myList):
    list_sort = [0] * 101
    for i in myList:
        list_sort[i] += 1
    for i in range(101):
        print((str(i) + ' ') * list_sort[i], end=' ')
myList = [int(i) for i in input().split()]
CountSort(myList)
