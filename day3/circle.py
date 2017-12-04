
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

def findway():
    size = 60
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    offset = size//2 + 1
    num = 1
    target = 289326
    matrix[offset][offset] = num


    i = 0
    j = 0
    step_x = True
    step = 1
    n = 1
    step_size = 1

    while num <= target:
        if step_x:
            i += step
        else:
            j += step
        n -= 1
        if n == 0:
            if not step_x:
                step = -step
                step_size += 1

            step_x = not step_x
            n = step_size
        num = neighbors(matrix, i, j, offset)
        matrix[i+offset][j+offset] = num
    return num

if __name__ == '__main__':
    findway()