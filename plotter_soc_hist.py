import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

rgbs = pd.read_csv("data_lucas_rgb.csv").to_numpy()

fig, ax = plt.subplots(1,1)

soc = rgbs[:,3]
counts, bins = np.histogram(soc)
ax.hist(bins[:-1], bins, weights=counts)
ax.set_title('SOC')



fig.tight_layout(pad=1.0)

plt.show()
