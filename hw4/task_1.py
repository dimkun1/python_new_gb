# Задача №1 домашнего задания 4. Транспонирование матрицы

def matrix_transposition(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end='\t')
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Исходная матрица:')
print_matrix(matrix)

new_matrix = matrix_transposition(matrix)
print('Полученная матрица:')
print_matrix(new_matrix)