def LongestCommonSubsequence(string1,string2):

    rows = len(string2)
    cols = len(string1)

    matrix = [[0 for i in range(cols+1)] for j in range(rows+1)]

    #Populate Matrix
    for row in range(1,rows+1):
        for col in range(1,cols+1):
            if string1[col-1] == string2[row-1]:
                matrix[row][col] = 1 + matrix[row-1][col-1]
            else:
                matrix[row][col] = max(matrix[row-1][col],matrix[row][col-1])

    #Generate Common Subsequence from the matrix
    j = cols
    i = rows
    seq = ''
    while j>0 and i>0:
        if string1[j-1] == string2[i-1]:
            seq += string1[j-1]
            i-=1
            j-=1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i-=1
        else:
            j-=1
    return(seq[::-1])

sequence = LongestCommonSubsequence('niranjan','raamanujan')
print(sequence)
