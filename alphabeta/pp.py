mnc = 0
abc = 0
def minmax(depth, node, ismax, values):
    global mnc
    if depth == 3:
        mnc += 1
        return values[node]
    if ismax:
        best = float("-inf")
        for i in range(2):
            value = minmax(depth+1,node*2+i,False,values)
            best = max(best,value)
        return best
    else:
        best = float("inf")
        for i in range(2):
            value = minmax(depth+1,node*2+i,True,values)
            best = min(best,value)
        return best
    
def alphabeta(depth,node,ismax,values,alpha,beta):
    global abc 
    if depth ==3:
        abc +=1
        return values[node]
    if ismax:
        best = float("-inf")
        for i in range(2):
            value = alphabeta(depth+1,node*2+i,False,values,alpha,beta)
            best = max(best,value)
            alpha = max(alpha,best)
            if beta <= alpha:
                break
        return best
    else:
        best = float("inf")
        for i in range(2):
            value = alphabeta(depth+1,node*2+i,True,values,alpha,beta)
            best = min(best,value)
            beta = min(beta,best)
            if beta<=alpha:
                break
        return best
    
values =[3, 5, 6, 9, 1, 2, 0, -1]
result = minmax(0,0,True,values)
resultalpha = alphabeta(0,0,True,values,float("-inf"),float("inf"))

print("Best value for minmax = ",result)
print("Best value for alphabeta = ",resultalpha)
print("Leaf Nodes Evaluated (Minimax):", mnc)
print("Leaf Nodes Evaluated (Alpha-Beta):", abc)