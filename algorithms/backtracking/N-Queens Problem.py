class NQueens:
    def __init__(self, n):
        self.n = n
        self.table = [[0 for _ in range(n)] for _ in range(n)]

    def print_table(self):
        for row in self.table:
            print(row)

    def is_safe(self, r, c):
        pass

nqueens = NQueens(4)
nqueens.print_table()
