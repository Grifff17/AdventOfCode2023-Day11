
def solvepart1():
    data = fileRead("test.txt")
    print(data)

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()