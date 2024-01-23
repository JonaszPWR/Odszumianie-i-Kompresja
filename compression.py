import numpy as np
import pywt
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from skimage import color

image = plt.imread('poohTest3.jpg').astype(float)
image = image[:,:,:3]
image = color.rgb2gray(image)
plt.imshow(image, plt.cm.gray)
plt.show()

compressFactor = 0.98

transformed = np.fft.ifft2(image)
coefficients = np.sort(np.abs(transformed.reshape(-1)))

threshold = coefficients[int(compressFactor * len(coefficients))]
indices = np.abs(transformed) > threshold

uncompressed = transformed * indices
imageOut = np.rot90(np.abs(np.fft.ifft2(uncompressed)), 2)

plt.imshow(imageOut, plt.cm.gray)
plt.show()