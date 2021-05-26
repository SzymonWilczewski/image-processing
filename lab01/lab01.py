from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage import color


# Exercise 1
print("Exercise 1")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)


# Exercise 2
print("Exercise 2")

print(np.shape(matrix))
print(matrix.shape)


# Exercise 3
print("Exercise 3")

print(matrix[0][1])


# Exercise 4
print("Exercise 4")

matrix[1][0] = 10
print(matrix)


# Exercise 5
print("Exercise 5")

for x in range(matrix.shape[0]):
    for y in range(matrix.shape[1]):
        if matrix[x][y] < 5:
            matrix[x][y] = 0
        else:
            matrix[x][y] = 1

print(matrix)


# Exercise 6

data_array = imread("python.png", True)
data_array = 1 - data_array
# Create a figure for plotting the data as a 3D histogram.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_data, y_data = np.meshgrid(np.arange(data_array.shape[1]), np.arange(data_array.shape[0]))
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = data_array.flatten()
ax.bar3d(x_data, y_data, np.zeros(len(z_data)), 1, 1, z_data)
# ax.view_init(42, 105)
# Finally, display the plot.
plt.show()
