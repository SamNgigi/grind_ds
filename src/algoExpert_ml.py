from typing import Sequence, Iterable, List, Dict, Tuple


def sparse_matrix_multiplication(matrix_a: List[List[int]], matrix_b: List[List[int]]) -> List[List[int]]:
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    sparse_a = get_dict_of_nonzero_cells(matrix_a);
    sparse_b = get_dict_of_nonzero_cells(matrix_b);

    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    return [[]]


def get_dict_of_nonzero_cells(matrix: List[List[int]])->Dict[Tuple, Int]:
    dict_of_nonzero_cells = {}
    for i in range(len(matrix): # Iterate through rows
        for j in range(len(matrix[0]): # Iterate through cols
    return dict_of_nonzero_cells
