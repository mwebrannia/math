# Define a Matrix A

A = [[5, 4, 3], 
     [2, 4, 6], 
     [4, 7, 9], 
     [8, 1, 3]]

# Define an empty Matrix of a reverse order

transpose_result = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

# Use nested for loop on Matrix A[]

for a in range (len(A)):
    for b in range (len(A[0])):                 # THIS IS THE LOGIC
        transpose_result[b][a] = A[a][b]

# Printing the results in the output

print("The transpose of Matrix A is: ")
for res in transpose_result:                    # THIS IS THE RESULT
    print(res)