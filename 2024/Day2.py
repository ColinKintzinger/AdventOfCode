
file = open("2024\\input_day_2.txt", "r")
cord= []
def importing_file():
    for line in file:
        line = list(map(int, line.strip().split()))
        cord.append(line)
importing_file()
print(cord)