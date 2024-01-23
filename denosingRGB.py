import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from skimage import color
from scipy import fftpack

"""
Niestety nie działa - nie udaje mi się poprawnie połączyć warstw kolorów, występują tylko dwie.
"""
im = plt.imread('deepfried_pooh.jpg').astype(float)
im = im[:,:,:3]
#im = color.rgb2gray(im)
plt.figure()
plt.imshow(im, plt.cm.gray)
plt.title('Original image')
plt.show()

channels = list()
for i in range(0, 2):
    current_im_fft = fftpack.fft2(im[:,:,i])
    keep_fraction = 0.1
    im_fft2 = current_im_fft.copy()
    r, c = im_fft2.shape
    im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0
    im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0
    new_im = fftpack.ifft2(im_fft2).real
    channels.append(new_im)
final_im = np.dstack(channels)


#display
plt.figure()
plt.imshow(final_im)
plt.title('Reconstructed Image')
plt.show()