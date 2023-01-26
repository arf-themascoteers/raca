import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

rgbs = pd.read_csv("data_lucas_hsv.csv").to_numpy()
a_sample = rgbs[1548,0:3]
# counts, bins = np.histogram(hue)
# print(counts)
# print(bins)
# plt.hist(bins[:-1], bins, weights=counts)
# plt.show()

thickness = 5
a_sample = a_sample*255
color = (a_sample[2],a_sample[1],a_sample[0])
print(color)
img = np.zeros((512,512,3), np.uint8)
img = cv2.rectangle(img, (0,0), (511,511), color, -1)

cv2.imshow("lalala", img)
k = cv2.waitKey(0) # 0==wait forever