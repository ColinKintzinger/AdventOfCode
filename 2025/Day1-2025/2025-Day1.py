class SafeDial:
    def __init__(self, size=100, start=50):
        self.size = size
        self.position = start % size
    
    def turn_right(self, amount):
        self.position = (self.position + amount) % self.size
    
    def turn_left(self, amount):
        self.position = (self.position - amount) % self.size

def readThroughFile(file, direction, movement):
    for line in file:
        line = line.strip()
        if line:
            tmp = line[0]
            dirtmp = int(line[1:])
            direction.append(tmp)
            movement.append(dirtmp)

def start_blunt_rotation(dial, direction, movementamount):
    counter = 0
    for i in range(len(direction)):
        if direction[i] == "L":
            dial.turn_left(movementamount[i])
            if dial.position == 0 : 
                counter += 1 
            
        if direction[i] == "R":
            dial.turn_right(movementamount[i])
            if dial.position == 0 : 
                counter += 1 
    return counter


file = open(r"2025\Day1-2025\input.txt", "r")
dial = SafeDial()
curent_Possition: int =dial.position
# testdirection = ["L","L","R","L","R","L","L","L","R","L"]
# testmovementamount = [68,30,48,5,60,55,1,99,14,82]
direction = []
movementamount= []
readThroughFile(file, direction, movementamount)
file.close()
counter=start_blunt_rotation(dial, direction, movementamount)
print(counter)

