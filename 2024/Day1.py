file = open("2024\\input.txt", "r")
row = 1000
col = 2
cord = []

for line in file:
    line = list(map(int, line.strip().split()))
    cord.append(line)
#cord.sort(cord[0])    
cord.sort(key=lambda x: (x[0]. x[1]))
#cord.sort(key= lambda x: x[1])
for row in cord:
    print(row)