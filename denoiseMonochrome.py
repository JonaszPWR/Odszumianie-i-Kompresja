import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from skimage import color
from scipy import fftpack

im = plt.imread('deepfried_pooh.jpg').astype(float)
im = im[:,:,:3]
im = color.rgb2gray(im)
plt.figure()
plt.imshow(im, plt.cm.gray)
plt.title('Original image')
plt.show()


current_im_fft = fftpack.fft2(im)
keep_fraction = 0.08 #lepsza wartość niż 0.1 lub 0.05
im_fft2 = current_im_fft.copy()
r, c = im_fft2.shape
im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0
im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0
final_im = fftpack.ifft2(im_fft2).real

#display
plt.figure()
plt.imshow(final_im, plt.cm.gray)
plt.title('Reconstructed Image')
plt.show()