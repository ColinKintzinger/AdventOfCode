file = open("2024\Day1\input_day_1.txt", "r")
row = 1000
col = 2
cord = []
left = []
right= []
distance = 0
sim = 0
def is_negative(num):
    if num < 0:
        return True
    return False
def finding_distance(left, right, distance ):
    tmp =0 
    for i in range(row):

        tmp = left[i] - right[i]
        if is_negative(tmp):
            tmp = tmp * -1
            distance += tmp
        else:
            distance += tmp
    return distance
def simularity_rating(left, right, sim):
    for i in range(row):
        count =0
        for j in range(row):
            if left[i] == right[j]:
                count += 1
        sim += left[i] * count
    return sim

for line in file:
    line = list(map(int, line.strip().split()))
    cord.append(line)
for i in range(row):
    left.append(cord[i][0])
    right.append(cord[i][1])
left.sort()
right.sort()
for i in range(row):
    cord[i][0] = left[i]
    cord[i][1] = right[i]

print ("Part 1:")
print (finding_distance(left, right, distance))
print ("Part 2:")
print (simularity_rating(left, right, sim))