minimax_count = 0
alphabeta_count = 0

def minimax(depth, node, ismax, values):
    global minimax_count

    if depth == 2:
        minimax_count += 1
        return values[node]

    if ismax:
        best = float("-inf")
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, False, values)
            best = max(best, value)
        return best

    else:
        best = float("inf")
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, True, values)
            best = min(best, value)
        return best


def alphabeta(depth, node, ismax, values, alpha, beta):
    global alphabeta_count

    if depth == 2:
        alphabeta_count += 1
        return values[node]

    if ismax:
        best = float("-inf")

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float("inf")

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

values =  [1,0,7,3]

minimax_result = minimax(0, 0, True, values)
alphabeta_result = alphabeta(0, 0, True, values, float("-inf"), float("inf"))

print("Minimax Result:", minimax_result)
print("Alpha-Beta Result:", alphabeta_result)
print("Leaf Nodes Evaluated (Minimax):", minimax_count)
print("Leaf Nodes Evaluated (Alpha-Beta):", alphabeta_count)