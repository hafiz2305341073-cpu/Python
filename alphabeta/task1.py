def minmax(depth,node,ismax,values):
    if depth == 2:
        return values[node]

    if ismax:
        best = float ("-inf")
        for i in range(2):
            value = minmax(depth+1,node*2+i,False,values)
            best = max(best,value)
        return best 

    else:
        best = float("inf")
        for i in range(2):
            value = minmax(depth+1, node*2+i,True,values)
            best = min(best,value)
        return best
    
values = list(map(int, input("Enter terminal values: ").split()))

if len(values) != 4:
    print("Please enter exactly 4 terminal values.")
else:
    result = minmax(0, 0, True, values)
    print("Best value is:", result)