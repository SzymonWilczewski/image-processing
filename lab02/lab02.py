from skimage.io import imread
from skimage import data
import matplotlib.pyplot as plt
from skimage import color
import numpy as np

# Exercise 1
print("Exercise 1")

# imRGB = imread('python.png')[:, :, :3]
imRGB = data.astronaut()


# Exercise 2
print("Exercise 2")

plt.imshow(imRGB)
plt.show()


# Exercise 3
print("Exercise 3")


# Exercise 4
print("Exercise 4")

imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray = color.lab2rgb(imLAB)

plt.figure(figsize=(20, 11))
plt.subplot(121), plt.imshow(imRGB), plt.axis('off'),
plt.title('original', size=20)
plt.subplot(122), plt.imshow(imRGBgray), plt.axis('off'),
plt.title('grayscale', size=20)
plt.show()


# Exercise 5
print("Exercise 5")

plt.imsave('grayscale.png', imRGBgray)


# Exercise 6
print("Exercise 6")

imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imLAB[..., 0] = imLAB[..., 0] - 75
imLAB[..., 0] = imLAB[..., 0].clip(min=0, max=100)
imRGBgraydark = color.lab2rgb(imLAB)

imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imLAB[..., 0] = imLAB[..., 0] + 75
imLAB[..., 0] = imLAB[..., 0].clip(min=0, max=100)
imRGBgraylight = color.lab2rgb(imLAB)

plt.figure(figsize=(20, 11))
plt.subplot(121), plt.imshow(imRGBgraydark), plt.axis('off'),
plt.title('lightness -75%', size=20)
plt.subplot(122), plt.imshow(imRGBgraylight), plt.axis('off'),
plt.title('lightness +75%', size=20)
plt.show()


# Exercise 7
print("Exercise 7")

# print(imRGBgray)
print(np.max(imRGBgray))
print(np.min(imRGBgray))

imRGBgray[imRGBgray > 0.3] = 1
imRGBgray[imRGBgray <= 0.3] = 0

# print(imRGBgray)
plt.imshow(imRGBgray)
plt.show()


# Exercise 8
print("Exercise 8")

# Threshold 0.1
imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray01 = color.lab2rgb(imLAB)

imRGBgray01[imRGBgray01 > 0.1] = 1
imRGBgray01[imRGBgray01 <= 0.1] = 0

# Threshold 0.5
imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray05 = color.lab2rgb(imLAB)

imRGBgray05[imRGBgray05 > 0.5] = 1
imRGBgray05[imRGBgray05 <= 0.5] = 0

# Threshold 0.9
imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray09 = color.lab2rgb(imLAB)

imRGBgray09[imRGBgray09 > 0.9] = 1
imRGBgray09[imRGBgray09 <= 0.9] = 0

plt.figure(figsize=(30, 11))
plt.subplot(131), plt.imshow(imRGBgray01), plt.axis('off'),
plt.title('threshold 0.1', size=20)
plt.subplot(132), plt.imshow(imRGBgray05), plt.axis('off'),
plt.title('threshold 0.5', size=20)
plt.subplot(133), plt.imshow(imRGBgray09), plt.axis('off'),
plt.title('threshold 0.9', size=20)
plt.show()


# Exercise 9
print("Exercise 9")

imRGBinverted = 255 - imRGB
imLAB = color.rgb2lab(imRGB)
imLABinverted = np.max(imLAB[..., 0]) - imLAB[..., 0]

plt.figure(figsize=(20, 11))
plt.subplot(121), plt.imshow(imRGBinverted), plt.axis('off'),
plt.title('RGB inverted', size=20)
plt.subplot(122), plt.imshow(imLABinverted), plt.axis('off'),
plt.title('LAB inverted', size=20)
plt.show()
