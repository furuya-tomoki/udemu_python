num = [[[0 for i in range(3)] for j in range(5)] for k in range(3)]

for k in range(3):
    num[0][0][k] = 1
    
for j in range(5):
    num[0][j][1] = 1
    
for j in range(3):
    num[1][0][k] = 1
    num[1][2][k] = 1
    
for j in range(5):
    num[1][j][0] = 1
    if j < 3:
        num[1][j][2] = 1
        
num[1][0][1] = 1
num[1][2][1] - 1

for i in range(5):
    num[2][j][0] = 1
    if(j == 0 or j == 4):
        num[2][j][1] = 1
    else:
        num[2][j][2] = 1
        
for i in range(3):
    for j in range(5):
        for k in range(3):
            if(num[i][j][k] == 1):
                print("■", end =" ")
            else:
                print("□", end =" ")
        print("")
    print("")