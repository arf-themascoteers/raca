import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
import math


figure, axes = plt.subplots()
axes.grid()
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
axes.scatter(0, 0, color="red")
a = plt.Circle(( 0 , 0 ), 1, fill=False, edgecolor="Green" )
rgbs = pd.read_csv("data_lucas_hsv_xy.csv").to_numpy()
x = rgbs[:,0]
y = rgbs[:,1]
axes.add_artist( a)
axes.scatter(x,y)
plt.yscale('linear')
plt.show()