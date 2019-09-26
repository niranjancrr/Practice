def LongestCommonSubstring(string1,string2):

    cols = len(string1)+1
    rows = len(string2)+1

    matrix = [[0 for j in range(cols)] for i in range(rows)]

    maximum = 0
    maxrow = 0
    maxcol=0
    for row in range(1,rows):
        for col in range(1,cols):
            if string1[col-1] == string2[row-1]:
                matrix[row][col] = matrix[row-1][col-1] + 1
                if matrix[row][col] > maximum:
                    maxrow = row
                    maxcol = col
                    maximum = matrix[row][col]
            

    #Generate Common Substring from the matrix
    seq = ''
    if maximum == 0:
        return seq
    else:
        j = maxcol
        i = maxrow
    
        while matrix[i][j] > 0:
            if string1[j-1] == string2[i-1]:
                seq += string1[j-1]
                i-=1
                j-=1
        return(seq[::-1])

sequence = LongestCommonSubstring('niranjan','raamanujan')
print(sequence)