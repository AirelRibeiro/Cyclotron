def cyclotron(particle, matrix_size):
    matrix = [["1"] * matrix_size for _ in range(matrix_size)]

    if particle == "e":
        for i in range(matrix_size):
            if i == 0 or i == matrix_size - 1:
                matrix[i] = [particle] * matrix_size
            else:
                matrix[i][-1] = particle

    elif particle == "p":
        for i in range(matrix_size):
            for j in range(matrix_size):
                if (
                    i == 0
                    or (i == matrix_size - 1 and j != matrix_size - 1)
                    or j == 0
                    or (j == matrix_size - 1 and i != matrix_size - 1)
                ):
                    matrix[i][j] = particle
                elif i == matrix_size - 2 and (
                    j == matrix_size - 2 or j == matrix_size - 1
                ):
                    matrix[i][j] = particle

    elif particle == "n":
        matrix[0] = [particle] * matrix_size

    for row in matrix:
        print(row)


