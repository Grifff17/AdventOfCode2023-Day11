
def solvepart1():
    #read in data
    data = fileRead("input.txt")
    smallUniverse = []
    for rowStr in data:
        row = []
        for i in rowStr.strip():
            row.append(i)
        smallUniverse.append(row)

    #expand universe
    tallUniverse = []
    for i in range(len(smallUniverse)): #expand vertically
        tallUniverse.append(smallUniverse[i])
        if (len(set(smallUniverse[i])) == 1):
            tallUniverse.append( ["*"] * len(tallUniverse[0]))
    universe = []
    for row in tallUniverse:
        universe.append(row.copy())
    numInserts = 0
    for i in range(len(tallUniverse[0])): #expand horizontally
        numGalaxys = 0
        for j in range(len(tallUniverse)):
            if tallUniverse[j][i] == "#":
                numGalaxys = numGalaxys + 1
        if numGalaxys == 0:
            for j in range(len(universe)):
                universe[j].insert(i+numInserts, "-")
            numInserts = numInserts + 1

    #generate list of galaxies
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[1])):
            if (universe[i][j] == "#"):
                galaxies.append([i,j])
    
    sum = 0
    for galaxy1index in range(len(galaxies)-1):
            for galaxy2index in range(galaxy1index+1, len(galaxies)):
                sum = sum + taxicabDistance(galaxies[galaxy1index],galaxies[galaxy2index])
    print(sum)

#returns taxicab distance between 2 points
def taxicabDistance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()