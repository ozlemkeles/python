# Given three integers x, y, and z representing the dimensions of a cuboid, and an integer n,
# find and print a list of all possible coordinates (i, j, k) on a 3D grid where the sum of (i + j + k) is not equal to n.
# Constraints: 1 <= i <= x, 1 <= j <= y, 1 <= k <= z.

# Example:
# Input:
#   x = 1
#   y = 1
#   z = 2
#   n = 3
# Output:
#   List of coordinates where (i + j + k) is not equal to 3: 
#[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_i = []
list_j = []
list_k = []

for i in range(x+1):
    list_i.append(i)
for j in range(y+1):
    list_j.append(j)
for k in range(z+1):
    list_k.append(k)

all_perm = [[i, j, k] for i in list_i
            for j in list_j
            for k in list_k
            if i+j+k != n]

print(all_perm)