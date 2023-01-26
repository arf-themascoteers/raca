import pandas as pd
import numpy as np

rgb_file = "rgb.csv"

npdf = pd.read_csv(rgb_file).to_numpy()
print("max")
print(np.max(npdf[:,0]))
print(np.max(npdf[:,1]))
print(np.max(npdf[:,2]))
print(np.max(npdf[:,3]))
print("min")
print(np.min(npdf[:,0]))
print(np.min(npdf[:,1]))
print(np.min(npdf[:,2]))
print(np.min(npdf[:,3]))

print("Done")
