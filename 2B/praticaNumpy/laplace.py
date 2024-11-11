import numpy as np

def laplace(mat) -> int:
    if mat.shape == (1,1):
        return mat[0][0]
    result = 0
    for j in range(mat.shape[1]):
        result += ((-1)**(1 + (j+1))) * mat[0, j] * laplace(np.delete(np.delete(mat, 0, 0), j, 1))
    return result

if __name__ == '__main__':
    mat = np.matrix([[1, 2, 3], [0, 4, 5], [1, 0, 6]])
    print(laplace(mat))