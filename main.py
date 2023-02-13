# Student number 40 26 00 33

# Constants
a = 0
b = 0
c = 3
d = 3

# 2D array of cells
T = [[0,c,c,0], [d,0,0,b], [d,0,0,b], [0,a,a,0]]

T11_old = 1.0
T12_old = 1.0
T21_old = 1.0
T22_old = 1.0

#Repeat for convergence
for count in range(10000):
  for i in range(1,3):
    for j in range(1,3):
      T[i][j] = (T[i-1][j] + T[i+1][j] + T[i][j-1] + T[i][j+1]) / 4
  
      # Calculate differences
      d11 = abs(T11_old - T[1][1])
      d12 = abs(T12_old - T[1][2])
      d21 = abs(T21_old - T[2][1])
      d22 = abs(T22_old - T[2][2])

  if d11 + d12 + d21 + d22 < 4E-11:
    break
  
  T11_old = T[1][1]
  T12_old = T[1][2]
  T21_old = T[2][1]
  T22_old = T[2][2]


print("T11 is", T[2][1])
print("T12 is", T[2][2])
print("T21 is", T[1][1])
print("T22 is", T[1][2])
