import pandas as pd
import numpy as np


def process():
    df = pd.read_csv("data_rgb_raw.csv")
    npdf = df.to_numpy()
    npdf[:, 0:3] = npdf[:, 0:3] / np.max(npdf[:, 0:3], axis = 0)
    print("max")
    print(npdf[:, 0].min())
    print(npdf[:, 1].min())
    print(npdf[:, 2].min())
    print("min")
    print(npdf[:, 0].max())
    print(npdf[:, 1].max())
    print(npdf[:, 2].max())
    df.to_csv("data_rgb.csv", index=False)
    print("done")


if __name__ == "__main__":
    process()