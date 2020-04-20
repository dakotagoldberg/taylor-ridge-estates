# Creating the Array
fieldSize = [7, 7]
global field
global trains
field = [[0 for x in range(fieldSize[0])] for y in range(fieldSize[1])] 
trains = []
playing = True

# trainFramework = [number, orientation, start, end, y/x val]

class Train:
    def __init__(self, number, orientation, startPos, endPos):
        self.number = number
        self.orientation = orientation
        self.startPos = startPos
        self.endPos = endPos

    def move(self, magnitude):
        if self.orientation == "horizontal":
            newStart = self.startPos[1] + magnitude
            newEnd = self.endPos[1] + magnitude
            if (magnitude > 0):
                greaterBound = newEnd
                lesserBound = self.startPos[1]
            else:
                lesserBound = newStart
                greaterBound = self.endPos[1]
            if (self.checkAvailableSpace(lesserBound, greaterBound, self.startPos[0])):
                self.startPos[1] = newStart
                self.endPos[1] = newEnd
            else:
                print("YOU CANNOT MOVE THE TRAIN")
        else:
            if self.orientation == "vertical":
                newStart = self.startPos[0] + magnitude
                newEnd = self.endPos[0] + magnitude
            if (magnitude > 0):
                greaterBound = newEnd
                lesserBound = self.startPos[0]
            else:
                lesserBound = newStart
                greaterBound = self.endPos[0]
            if (self.checkAvailableSpace(lesserBound, greaterBound, self.startPos[1])):
                self.startPos[0] = newStart
                self.endPos[0] = newEnd
            else:
                print("YOU CANNOT MOVE THE TRAIN")

    def checkAvailableSpace(self, lesserBound, greaterBound, track):
        if self.orientation == "horizontal":
            for i in range(lesserBound, greaterBound + 1):
                if i >= lesserBound and i <= greaterBound:
                    if (i < 0 or i >= len(field[0])) or (field[track][i] != 0 and field[track][i] != self.number):
                        return False
        if self.orientation == "vertical":
            for i in range(lesserBound, greaterBound + 1):
                if i >= lesserBound and i <= greaterBound:
                    if (i < 0 or i >= len(field)) or (field[i][track] != 0 and field[i][track] != self.number):
                        return False
        return True


def generateTrains():
    # NOTE: [a, b] --> a is up/down, b is left/right
    tom = Train(1, "horizontal", [1, 1], [1, 2])
    tom3 = Train(3, "vertical", [1, 5], [3, 5])
    trains.append(tom)
    trains.append(tom3)


def getExistingTrains():
    lineup = []
    for i in trains:
        lineup.append(i.number)
    
    return lineup

def renderField():
    field = [[0 for x in range(fieldSize[0])] for y in range(fieldSize[1])] 
    for i in trains:
        if i.orientation == "horizontal":
            for n in range(len(field[0])):
                if (n >= i.startPos[1] and n <= i.endPos[1]):
                    field[i.startPos[0]][n] = i.number
        else:
            for n in range(len(field)):
                if (n >= i.startPos[0] and n <= i.endPos[0]):
                    field[n][i.startPos[1]] = i.number

    return field

def printField(field):
    for i in field:
            for j in i:
                print(j, end = " "),
            print("")

def operateField():
    while (playing):
        field = renderField() #THIS MUST GO FIRST
        printField(field)
        print("\n")
        print("Type the train number you would like\nto move and how far you want to move it: ", end = " ")
        commands = input()
        commandList = commands.split(" ")
        try:
            trainToOperate = int(commandList[0])
        except:
             print("You can only enter integers.")
             continue
        
        try:
            distance = int(commandList[1])
        except:
             print("You can only enter integers.")
             continue
        # if type(commandList[0]) != int or type(commandList[1]) != int:
        #     print("You can only enter integers.")
        #     continue
        if trainToOperate not in getExistingTrains():
            print("That train literally isn't even on the board.")
            continue
        trains[getExistingTrains().index(trainToOperate)].move(distance)


# generateTrains()
# operateField()

print("Before the move:\n")
generateTrains()
field = renderField() #THIS MUST GO FIRST
printField(field)
trains[1].move(-1)
trains[0].move(1)
trains[0].move(1)
trains[0].move(1)
print("After the move:\n")
field = renderField() #THIS MUST GO FIRST
printField(field)