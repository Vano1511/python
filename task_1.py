class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            new_list.append([])
            for j in range(len(self.list[i])):
                new_list[i].append(self.list[i][j] + other.list[i][j])
        return new_list


matr1 = Matrix([[3, 2, 4], [7, 4, 8]])
matr2 = Matrix([[7, 4, 8], [4, 2, 7]])
print(matr2)
print(matr1)
matr3 = Matrix(matr2 + matr1)
print(matr3)