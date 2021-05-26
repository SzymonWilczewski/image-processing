from skimage.io import imread
import matplotlib.pyplot as plt
from skimage import color

imRGB = imread('new_york.jpg')

imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray = color.lab2rgb(imLAB)

plt.imsave('new_york_gray.png', imRGBgray)


imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray9 = color.lab2rgb(imLAB)

imRGBgray9[imRGBgray9 <= 0.2] = 0.2
imRGBgray9[(0.2 < imRGBgray9) & (imRGBgray9 <= 0.3)] = 0.3
imRGBgray9[(0.3 < imRGBgray9) & (imRGBgray9 <= 0.4)] = 0.4
imRGBgray9[(0.4 < imRGBgray9) & (imRGBgray9 <= 0.5)] = 0.5
imRGBgray9[(0.5 < imRGBgray9) & (imRGBgray9 <= 0.6)] = 0.6
imRGBgray9[(0.6 < imRGBgray9) & (imRGBgray9 <= 0.7)] = 0.7
imRGBgray9[(0.7 < imRGBgray9) & (imRGBgray9 <= 0.8)] = 0.8
imRGBgray9[(0.8 < imRGBgray9) & (imRGBgray9 <= 0.9)] = 0.9
imRGBgray9[0.9 < imRGBgray9] = 1

plt.imsave('9ShadesOfGray.png', imRGBgray9)


imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray5 = color.lab2rgb(imLAB)

imRGBgray5[imRGBgray5 <= 0.2] = 0.2
imRGBgray5[(0.2 < imRGBgray5) & (imRGBgray5 <= 0.4)] = 0.4
imRGBgray5[(0.4 < imRGBgray5) & (imRGBgray5 <= 0.6)] = 0.6
imRGBgray5[(0.6 < imRGBgray5) & (imRGBgray5 <= 0.8)] = 0.8
imRGBgray5[0.8 < imRGBgray5] = 1

plt.imsave('5ShadesOfGray.png', imRGBgray5)


imLAB = color.rgb2lab(imRGB)
imLAB[..., 1] = imLAB[..., 2] = 0
imRGBgray2 = color.lab2rgb(imLAB)

imRGBgray2[imRGBgray2 <= 0.5] = 0
imRGBgray2[imRGBgray2 > 0.5] = 1

plt.imsave('2ShadesOfGray.png', imRGBgray2)
