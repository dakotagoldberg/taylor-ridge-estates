from random import randint
from time import sleep

# Creating the Array
fieldSize = [6, 6]
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
        field = renderField()
        if self.orientation == "horizontal":
            newStart = self.startPos[1] + magnitude
            newEnd = self.endPos[1] + magnitude
            if (magnitude > 0):
                greaterBound = newEnd
                lesserBound = self.startPos[1]
            else:
                lesserBound = newStart
                greaterBound = self.endPos[1]
            if (self.checkAvailableSpace(lesserBound, greaterBound, self.startPos[0], field)):
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
            if (self.checkAvailableSpace(lesserBound, greaterBound, self.startPos[1], field)):
                self.startPos[0] = newStart
                self.endPos[0] = newEnd
            else:
                print("YOU CANNOT MOVE THE TRAIN")

    def checkAvailableSpace(self, lesserBound, greaterBound, track, field):
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
    
    goalTrain = Train(1, "horizontal", [2, 0], [2, 1])
    trains.append(goalTrain)
    
    numTrains = randint(9, 15)
    for i in range(2, numTrains):
        trainPassesInspection = False
        tryCounter = 0
        field = renderField()
        while(not trainPassesInspection and tryCounter < 1000):
            direction = 2 % randint(2, 6) # 1 --> horizontal, 0 --> vertical
            shift = randint(0, fieldSize[0] - 1)
            startPlace = randint(0, 4)
            length = randint(2, 3)
            tryCounter+=1
            if (direction):
                startPos = [shift, startPlace]
                endPos = [shift, startPlace + length - 1]
                tempTrain = Train(i, "horizontal", startPos, endPos)
                trainPassesInspection = tempTrain.checkAvailableSpace(startPlace, startPlace + length - 1, shift, field)                
                # print(trainPassesInspection)
                field = renderField()
                if (trainPassesInspection and checkImpossible(tempTrain)):
                    trains.append(tempTrain)
            else:
                startPos = [startPlace, shift]
                endPos = [startPlace + length - 1, shift]
                tempTrain = Train(i, "vertical", startPos, endPos)
                trainPassesInspection = tempTrain.checkAvailableSpace(startPlace, startPlace + length - 1, shift, field)
                # print(trainPassesInspection)
                field = renderField()
                if (trainPassesInspection and checkImpossible(tempTrain)):
                    trains.append(tempTrain)
        
        # print("train: " + str(i) + " direction: " + str(direction) +  " shift: " + str(shift) +  " startPos: " + str(startPlace) +  " length: " + str(length))

    shuffleTrains()
    
# def shuffleTrains():
#     field = renderField()
#     for i in range(1000):
#         field = renderField()
#         randomTrain = randint(1, len(trains))
#         randomDistance = randint(1, 4)
#         trains[getExistingTrains().index(randomTrain)].move(randomDistance)
#         field = renderField()
#         trains[getExistingTrains().index(1)].move(-1)
#         field = renderField()
def shuffleTrains():
    field = renderField()
    for j in range(100):
        for i in range(2, len(trains)):
            if i not in getExistingTrains():
                print("That train literally isn't even on the board.")
                continue
            field = renderField()
            randomDistance = randint(1, 4)
            trains[getExistingTrains().index(i)].move(randomDistance)
            field = renderField()
        trains[getExistingTrains().index(1)].move(-1)



def checkInstantWin():
    field = renderField()
    firstOne = field[2].index(1)
    for i in (field[2][firstOne:len(field[2])]):
        if i != 0 and i != 1:
            return False
    return True

def checkImpossible(train):
    field = renderField()
    if train.orientation == "horizontal" and train.startPos[0] == 2:
        return False
    elif train.orientation == "vertical":
        for i in range(train.startPos[0], train.endPos[0] + 1):
            if i == 2:
                return False
    return True


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
                print(hex(j)[-1], end = " "),
            print("")


totalTrophies = 0
while (object):
    trains = []
    field = renderField()
    generateTrains()
    field = renderField()
    while (checkInstantWin() == True):
        trains = []
        generateTrains() # Generate the trains before they move because if there are no trains then how are we supposed...
        field = renderField()
    # PLAY

    while (playing):
        field = renderField() #THIS MUST GO FIRST
        printField(field)
        if (trains[0].startPos == [2, 4]):
            print("You Won! Here is your trophy: 🏆")
            totalTrophies += 1
            print("Total trophies: " + str(totalTrophies) + "🏆")
            sleep(3)
            break
        print("\n")
        print("Type the train number you would like\nto move and how far you want to move it: ", end = " ")
        commands = input()
        commandList = commands.split(" ")
        try:
            trainToOperate = int(commandList[0], 16)
        except:
                print("You can only enter integers.")
                continue
        
        try:
            distance = int(commandList[1])
        except:
                print("You can only enter integers.")
                continue

        if trainToOperate not in getExistingTrains():
            print("That train literally isn't even on the board.")
            continue
        trains[getExistingTrains().index(trainToOperate)].move(distance)

