def Pasacal_triangle(no_rows):
    pasacal_list=[[] for i in range(no_rows)]
    for i in range(no_rows):
        for j in range(i+1):
            if(j==0):
                pasacal_list[i].append(1)
            elif(i==j):
                pasacal_list[i].append(1)
            else:    
                left_right_add=pasacal_list[i-1][j-1]+pasacal_list[i-1][j]
                pasacal_list[i].append(left_right_add)
                
    return pasacal_list
    
print(Pasacal_triangle(5))   
print(0<0)
