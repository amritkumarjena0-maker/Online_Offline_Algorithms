# Program 2: Matrix-Chain Multiplication Using Dynamic Programming

def matrix_chain_multiplication():
    print("\n--- Matrix-Chain Multiplication ---")

    n = int(input("Enter number of matrices: "))

    if n <= 0:
        print("Number of matrices must be greater than zero.")
        return

    p = []

    print("Enter the dimensions array:")

    for i in range(n + 1):
        dimension = int(input(f"p[{i}] = "))

        if dimension <= 0:
            print("Dimensions must be greater than zero.")
            return

        p.append(dimension)

    cost = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            cost[i][j] = float("inf")

            for k in range(i, j):
                current = (
                    cost[i][k]
                    + cost[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if current < cost[i][j]:
                    cost[i][j] = current
                    split[i][j] = k

    print(
        "\nMinimum number of scalar multiplications:",
        cost[1][n]
    )

    def print_order(i, j):
        if i == j:
            print(f"A{i}", end="")
        else:
            print("(", end="")
            print_order(i, split[i][j])
            print_order(split[i][j] + 1, j)
            print(")", end="")

    print("Optimal multiplication order: ", end="")
    print_order(1, n)
    print()


if __name__ == "__main__":
    matrix_chain_multiplication()