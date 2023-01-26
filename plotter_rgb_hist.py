import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

rgbs = pd.read_csv("data_lucas_rgb.csv").to_numpy()

fig, ax = plt.subplots(1,3)

red = rgbs[:,0]
counts, bins = np.histogram(red)
ax[0].hist(bins[:-1], bins, weights=counts, color = "Red")
ax[0].set_title('Red')
ax[0].set_xlim([0, 1])

green = rgbs[:,1]
counts, bins = np.histogram(green)
ax[1].hist(bins[:-1], bins, weights=counts, color = "Green")
ax[1].set_title('Green')
ax[1].set_xlim([0, 1])

blue = rgbs[:,2]
counts, bins = np.histogram(blue)
ax[2].hist(bins[:-1], bins, weights=counts, color = "Blue")
ax[2].set_title('Blue')
ax[2].set_xlim([0, 1])

fig.tight_layout(pad=1.0)

plt.xlim(0,1)
plt.show()
