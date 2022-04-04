# Python has a built-in type called 'list' which allows us to store different values in a indexed way
my_list = [5, 2, 9, 1, 7]

# Indexing always starts at 0!
print("First element =", my_list[0])
print("Fourth element =", my_list[3])

# Lists can contain any type
# They can be useful, but they don't have some of the mathematical functionality that we want
# e.g. adding vectors, multiplying vectors by a scalar

# Numpy is a popular library for maths & mathematical structures
# numpy arrays are very common in python programs!
# vectors and matrices can be modeled using numpy arrays very easily
import numpy as np

# Creating a numpy array
v1 = np.array([2, 1.5, 0.5])
v2 = np.array([1.0, 0.5, 3.0])

# We can make them whatever size we like
# here are some ways of initialising arrays with a choice of size
# there are lots of ways to generate and initialise numpy arrays!
v3 = np.array([0.]*1000)  # 1000 zeroes
v4 = np.zeros(1000)       # also 1000 zeroes!
v5 = np.ones(50)          # 50 ones
v6 = np.ones(25)*3        # 25 threes
v7 = np.array([3.0]*25)   # also 25 threes

# we can find a value at a given index as before
print("Second element of v1 = ", v1[1])

# we can print arrays
print("v1 =", v1, "v2 = ", v2)

# adding arrays together, element-wise
print("v1 + v2 =", v1 + v2)

# add a number to each component of a array
print("v1 + 2 = ", v1 + 2.0)

# multiply by a scalar
print("2 times v1 = ", 2.0*v1)

# be careful: arithmetic like multiplication is element-wise as well
print("v1 * v2 = ", v1*v2)

# If we want a dot product we have to call a different method
print("v1 . v2 = ", np.dot(v1, v2))

# We also use conditionals with arrays: this results in an array of true/false values
print("v1 < v2", v1 < v2)
print("v1 >= 1.0", v1 >= 1)


# We can access or modify multiple elements by using a list of indices
index_list = [0, 2]
print("first and last elements of v1 are: ", v1[index_list])

# Or we can use a mask: true / false values for each index. This is useful for conditionals!
# for example here we double all the values in v1 which are less than the corresponding value in v2
mask = v1 < v2
print("masked elements of v1: ", v1[mask])
v1[mask] *= 2
print("doubling masked elements:", v1)


# defining functions with vectors is the same as before
# e.g. this function calculates a weighted sum of two vectors
# then returns for which elements the result is less than one
def f_vec(x, y, a):
    v = a * x + y
    return v < 1.0


print("f_vec(v1, v2) =", f_vec(v1, v2, 0.2))


# We can also have higher dimensional arrays, e.g. Matrices can be modeled as 2D arrays
# We can initialise with a list of lists, i.e. a comma separated list where each element is itself a list!
Identity_Matrix = np.array([[1., 0., 0.],
                            [0., 1., 0.],
                            [0., 0., 1.]])

# The above formatting is optional but can make things clearer
Another_Matrix = np.array([[1., 0.5, 0.3], [0.1, 1.5, 2.0], [3.3, 9.9, 6.2]])

# Addition etc. still applies element-wise
Sum_Matrix = Identity_Matrix + Another_Matrix

# We access elements with two separate indices like so (remember indexing starts at 0):
print("I_00 = ", Identity_Matrix[0][0])
print("A_21 = ", Another_Matrix[2][1])

# There is much more functionality available when and if you need it!
