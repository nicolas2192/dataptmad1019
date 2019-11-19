#1. Import the NUMPY package under the name np.
import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2,3,5))

#4. Print a.
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.random.random((5,2,3))

#6. Print b.
print("Exercise 6")
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?
if a.size == b.size:
    print(f"Arrays A and B have the same size: {a.size}")

#8. Are you able to add a and b? Why or why not?
if a.shape != b.shape:
    print(f"You cannot add two arrays with different shapes. A = {a.shape} and B = {b.shape}")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = b.reshape(2,3,5)
print(c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
if a.shape == c.shape:
    d = a + c
print(d)  #it works because both arrays have the same shape

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("ejercicio 11")
print(a)
print(d)  #items in array d are bigger than those in array a since array d is a result of adding arrays a and c

#12. Multiply a and c. Assign the result to e.
e = a * c

#13. Does e equal to a? Why or why not?
print("Ejercicio 13")

print("Equal!" if np.array_equal(a,e) else "not equal")

if np.array_equal(a,e):
    print("Equal!")
else:
    print("not equal")

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print("Exercise 14")
d_max = d.max()
d_min = d.min()
d_mean = np.mean(d)

print(f"The minimum value is: {d_min}")
print(f"The mean value is: {d_mean}")
print(f"The maximum value is: {d_max}")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for x in range(2):
    for y in range(3):
        for z in range(5):
            if d_min < d[x][y][z] < d_mean:
                f[x, y, z] = 25
            if d_mean < d[x][y][z] < d_max:
                f[x, y, z] = 75
            if d[x][y][z] == d_mean:
                f[x, y, z] = 50
            if d[x][y][z] <= d_min:
                f[x, y, z] = 0
            if d[x][y][z] >= d_max:
                f[x, y, z] = 100


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(d)
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
let = np.chararray((2,3,5))

for x in range(2):
    for y in range(3):
        for z in range(5):
            if f[x, y, z] == 25:
                let[x, y, z] = "D"
            if f[x, y, z] == 75:
                let[x, y, z] = "B"
            if f[x, y, z] == 50:
                let[x, y, z] = "C"
            if f[x, y, z] == 0:
                let[x, y, z] = "E"
            if f[x, y, z] == 100:
                let[x, y, z] = "A"

print(let)

print(let[0][2][3])

