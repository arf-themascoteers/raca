import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

rgbs = pd.read_csv("data_lucas_hsv.csv").to_numpy()
#plt.xlim(0,1)
fig, ax = plt.subplots(1,3)

hue = rgbs[:,0]
counts, bins = np.histogram(hue)
ax[0].hist(bins[:-1], bins, weights=counts)
ax[0].set_title('Hue')
ax[0].set_xlim([0, 1])

value = rgbs[:,1]
counts, bins = np.histogram(value)
ax[1].hist(bins[:-1], bins, weights=counts)
ax[1].set_title('Value')
ax[1].set_xlim([0, 1])

saturation = rgbs[:,2]
counts, bins = np.histogram(saturation)
ax[2].hist(bins[:-1], bins, weights=counts)
ax[2].set_title('Saturation')
ax[2].set_xlim([0, 1])

fig.tight_layout(pad=1.0)


plt.show()
