inputFile = open('C:/PYTHON/Task 6/practise6/input.txt', 'r', encoding='utf-8')
sortirovka = []
for line in inputFile:
    line = line.split()
    line.pop(2)
    sortirovka.append(line)
inputFile.close()
sortirovka.sort()
for i in sortirovka:
    for j in i:
        print(j, end=' ')
    print()
