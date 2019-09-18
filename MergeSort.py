
def merge(jumbledlist,low,middle,high):

    i = j = 0
    k = low
    firsthalf = jumbledlist[low:middle]
    secondhalf = jumbledlist[middle:high]
    #print(firsthalf,secondhalf)
    while i<(middle-low) and j<(high-middle):
        if firsthalf[i]>secondhalf[j]:
            jumbledlist[k]=secondhalf[j]
            j+=1
        else:
            jumbledlist[k]=firsthalf[i]
            i+=1
        k+=1
    while i<(middle-low):
        jumbledlist[k] = firsthalf[i]
        i+=1
        k+=1
    while j<(high-middle):
        jumbledlist[k] = secondhalf[j]
        j+=1
        k+=1

def mergesort(jumbledlist,low,high):

    if (high-low) <= 1:
        return
    else:
        middle = int((low+high)/2)
        mergesort(jumbledlist,low,middle)
        mergesort(jumbledlist,middle,high)
        merge(jumbledlist,low,middle,high)

    #print(jumbledlist)

if __name__ == '__main__':
    jumbledlist = [9,8,7,6,5,4,3,2,1,0]
    print(jumbledlist)
    mergesort(jumbledlist,0,len(jumbledlist))
    print(jumbledlist)