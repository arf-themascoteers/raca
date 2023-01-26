import pandas as pd
import colour
import numpy as np


def process(inf, outf):
    df = pd.read_csv(inf)
    npdf = df.to_numpy()
    for i in range(len(npdf)):
        npdf[i,0:3] = colour.RGB_to_HSV(npdf[i,0:3])
    # max_values = np.max(npdf[:, 0:3], axis=0).reshape(1,-1)
    # npdf[:, 0:3] = npdf[:, 0:3] / max_values
    print(npdf[:, 0].min())
    print(npdf[:, 1].min())
    print(npdf[:, 2].min())
    print(npdf[:, 0].max())
    print(npdf[:, 1].max())
    print(npdf[:, 2].max())
    df = pd.DataFrame(npdf, columns = ['h','s','v','oc'])
    df.to_csv(outf, index=False)
    print("done")


if __name__ == "__main__":
    process("data_lucas_rgb.csv", "data_lucas_hsv.csv")