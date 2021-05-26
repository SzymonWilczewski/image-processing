from skimage.io import imread
import matplotlib.pyplot as plt
from skimage import color
from skimage.transform import rescale

imRGB = imread('new_york.jpg')

imGRAY = color.rgb2gray(imRGB)

imGRAY_rescaled_5 = rescale(imGRAY, 0.05, anti_aliasing=False)
imGRAY_rescaled_2 = rescale(imGRAY, 0.02, anti_aliasing=False)
imGRAY_rescaled_1 = rescale(imGRAY, 0.01, anti_aliasing=False)

plt.imsave('downsampling5.png', imGRAY_rescaled_5, cmap="gray")
plt.imsave('downsampling2.png', imGRAY_rescaled_2, cmap="gray")
plt.imsave('downsampling1.png', imGRAY_rescaled_1, cmap="gray")
