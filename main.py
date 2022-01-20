
# 3  * 3
from operator import le
from tkinter.messagebox import RETRY


def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o


def sum(A, B):
    output = []
    for i in range(len(A)):  # no of rows
        row = []
        for j in range(len(A[0])):  # no of culms
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


if __name__ == "__main__":

    inputM = int(input("Enter the value of m:\n"))
    inputN = int(input("Enter the value of n:\n"))

    print("Enter Matrix A")

    A = matrix(inputM, inputN)

    print("Enter Matrix B")
    B = matrix(inputM, inputN)
    print(f"A = {A}\nB = {B}")
    s = sum(A, B)
    print(f"Sum A & B = {s}")
