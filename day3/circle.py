
def neighbors(matrix, i=0, j=0, offset=0):
    """find sum of neighbor"""
    num = matrix[i-1+offset][j-1+offset] + matrix[i-1+offset][j+offset] + \
        matrix[i-1+offset][j+1+offset] + matrix[i+offset][j+1+offset] + \
        matrix[i+offset][j-1+offset] + matrix[i+1+offset][j-1+offset] + \
        matrix[i+1+offset][j+offset] + matrix[i+1+offset][j+1+offset]
    return(num)

def set_node(matrix, i=0, j=0, offset=0):
    """set node to sum of neighbor"""
    matrix[i+offset][j+offset] = neighbors(matrix, 0, 0, 0)
    return matrix

if __name__ == '__main__':
    findway()