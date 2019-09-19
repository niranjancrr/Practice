def getMultiplesEvenOrOdd(number):
    multiples = []
    for div in range(1,number+1):
        if float(number)%div == 0.0:
            multiples.append(div)
    if (float(len(multiples)))%2 == 0.0:
        return "even"
    else:
        return "odd"

def countOpenDoors():
    doorList = [0] * 100

    for counter,_ in enumerate(doorList):
        if getMultiplesEvenOrOdd(counter+1) == 'even':
            doorList[counter] = 0
        else:
            doorList[counter] = 1

    openDoors = doorList.count(1)

    print('Number of Open Doors = {}' .format(openDoors))
    return openDoors

if __name__ == '__main__':
    countOpenDoors()

