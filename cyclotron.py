def cyclotron(particle, matrix_size):
    matrix = [["1"] * matrix_size for _ in range(matrix_size)]

    if particle == "e":
        for i in range(matrix_size):
            if i == 0 or i == matrix_size - 1:
                matrix[i] = [particle] * matrix_size
            else:
                matrix[i][-1] = particle
