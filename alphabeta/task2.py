def minimax(depth, node, ismax, values):
    if depth == 2:
        return values[node], []
    if ismax:
        best = float("-inf")
        best_path = []
        for i in range(2):
            value, path = minimax(depth + 1, node * 2 + i, False, values)

            if value > best:
                best = value
                best_path = [("Left" if i == 0 else "Right")] + path
        return best, best_path
    else:
        best = float("inf")
        best_path = []
        for i in range(2):
            value, path = minimax(depth + 1, node * 2 + i, True, values)

            if value < best:
                best = value
                best_path = [("Left" if i == 0 else "Right")] + path

        return best, best_path

values = list(map(int, input("Enter terminal values: ").split()))

if len(values) != 4:
    print("Please enter exactly 4 terminal values.")
else:
    result, path = minimax(0, 0, True, values)
    print("Optimal Value =", result)
    print("\nSelected Path:")
    print("Root")
    for direction in path:
        print("↓")
        print(direction)