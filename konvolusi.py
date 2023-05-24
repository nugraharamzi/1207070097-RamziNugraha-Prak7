import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

import cv2

citra1 = imread(fname="gedung.tif")
print(citra1.shape)

plt.imshow(citra1, cmap='gray')

kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap = 'gray')
ax[1].set_title("Citra Output")