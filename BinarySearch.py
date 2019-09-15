
def BinarySearch(searchList,low,high,value):

    middle = int((low+high)/2)

    if middle >= len(searchList) or middle <= 0:
        print('value {} was not found in searchList' .format(value))
        return False

    if searchList[middle] == value:
        print('Found {} at postion {}' .format(value,middle))
        return True
    elif value < searchList[middle]: 
        return BinarySearch(searchList,low,middle,value)
    else:
        return BinarySearch(searchList,middle+1,high,value)

if __name__ == '__main__':
    searchList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(BinarySearch(searchList,0,len(searchList),10))
    print(BinarySearch(searchList,0,len(searchList),-1))
    print(BinarySearch(searchList,0,len(searchList),16))
