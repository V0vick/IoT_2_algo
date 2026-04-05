import os

def read_input(filename="career.in"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    with open(filepath, "r") as f:
        L = int(f.readline().strip())
        pyramid = []
        for _ in range(L):
            row = list(map(int, f.readline().split()))
            pyramid.append(row)
    return L, pyramid


def compute_max_experience(L, pyramid):
    dp = pyramid[-1][:]

    for i in range(L - 2, -1, -1):
        new_dp = []
        for j in range(len(pyramid[i])):
            best_below = max(dp[j], dp[j + 1])
            new_dp.append(pyramid[i][j] + best_below)
        dp = new_dp

    return dp[0]


def main():
    L, pyramid = read_input()
    result = compute_max_experience(L, pyramid)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "career.out")
    with open(out_path, "w") as f:
        f.write(str(result) + "\n")


if __name__ == "__main__":
    main()