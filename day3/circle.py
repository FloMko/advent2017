
def neighbors(matrix, i=0, j=0, offset=0):
    num = matrix[i-1+offset][j-1+offset] + matrix[i-1+offset][j+offset] + \
        matrix[i-1+offset][j+1+offset] + matrix[i+offset][j+1+offset] + \
        matrix[i+offset][j-1+offset] + matrix[i+1+offset][j-1+offset] + \
        matrix[i+1+offset][j+offset] + matrix[i+1+offset][j+1+offset]
    return(num)
if __name__ == '__main__':
    findway()