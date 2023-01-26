import pandas as pd
import numpy as np
import math


def get_x_y(h):
    angle = 2 * math.pi * h
    x = math.cos(angle)
    y = math.sin(angle)
    return x,y


def process(inf, outf):
    df = pd.read_csv(inf)
    npdf = df.to_numpy()
    mydata = np.zeros((npdf.shape[0],npdf.shape[1]+1))
    mydata[:,2:] = npdf[:,1:]
    for i in range(len(npdf)):
        x,y = get_x_y(npdf[i,0])
        mydata[i,0] = x
        mydata[i,1] = y

    print(mydata[:, 0].min())
    print(mydata[:, 1].min())
    print(mydata[:, 2].min())
    print(mydata[:, 3].min())
    print(mydata[:, 0].max())
    print(mydata[:, 1].max())
    print(mydata[:, 2].max())
    print(mydata[:, 3].max())

    df = pd.DataFrame(mydata, columns = ['HX', 'HY', 'S','V','oc'])
    df.to_csv(outf, index=False)
    print("done")



if __name__ == "__main__":
    process("data_lucas_rgb.csv", "data_lucas_hsv_xy.csv")
