
file = open("2024\\input_day_2.txt", "r")
cord= []
def importing_file():
    for line in file:
        line = list(map(int, line.strip().split()))
        cord.append(line)
def check_list(cord):
    for i in range(len(cord)):
        for j in range(len(cord[i])-1):
            pass
importing_file()
print(cord)