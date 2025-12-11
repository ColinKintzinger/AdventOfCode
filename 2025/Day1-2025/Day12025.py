class SafeDial:
    def __init__(self, size=99, start=50):
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

# def start_blunt_rotation(dial, direction, movementamount):





file = open("2025\Day1-2025\input.txt", "r")
dial = SafeDial()
curent_Possition: int =dial.position
counter: int = 0
direction = []
movementamount = []
readThroughFile(file, direction, movementamount)
