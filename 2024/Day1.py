file = open("2024\\input.txt", "r")
cord = [[]]

# Read each line from the file
#lines = file.readlines()
def get_file_data():
    for line in file:
        # Split the line into columns and convert to integers if necessary
        
        columns = line.strip().split()

        cord.append(columns)
    file.close()
def tranposing(col, row, cord):
    tr = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            tr[j][i] = cord[i][j]
    return tr
def row_wise_sort(M):
    for i in range(len(M)):
        M[i] = sorted(M[i])
    return M

def sort_col(col, row, cord):

    B= tranposing(col, row, cord)
    
# Print the 2D array
for row in cord:
    print(row)

