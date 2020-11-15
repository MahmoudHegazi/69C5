main = [1,2,3,4,5]
for side in main:
    for x in main:
        if side == x:
            continue
        else:
            print(str(side) + ',' + str(x))
    
