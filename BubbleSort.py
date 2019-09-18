def bubblesort(jumbledlist):

    for i in range(len(jumbledlist)-1):
        for j in range(i,len(jumbledlist)):
            if jumbledlist[i]>jumbledlist[j]:
                jumbledlist[i],jumbledlist[j]=jumbledlist[j],jumbledlist[i]

if __name__ == '__main__':
    jumbledlist = [9,8,7,6,5,4,3,2,1,0]
    print(jumbledlist)
    bubblesort(jumbledlist)
    print(jumbledlist)