from sklearn.linear_model import LinearRegression
import numpy as np
import ds_manager
from scipy.stats import pearsonr

def calculate_r2(train_ds, test_ds):
    train_x = train_ds.get_x()
    train_y = train_ds.get_y()
    test_x = test_ds.get_x()
    test_y = test_ds.get_y()

    r1 = pearsonr(train_x[:,0], train_y)
    r2 = pearsonr(train_x[:,1], train_y)
    r3 = pearsonr(train_x[:,2], train_y)

    return r1.statistic, r2.statistic, r3.statistic


def r2(dm):
    i0s = []
    i1s = []
    i2s = []
    for train_ds, test_ds in dm.get_10_folds():
        i0, i1, i2 = calculate_r2(train_ds, test_ds)
        print(i0, i1, i2)
        i0s.append(i0)
        i1s.append(i1)
        i2s.append(i2)

    return i0s, i1s, i2s


dm = ds_manager.DSManager("lucas", "hsv")
i0s, i1s, i2s = r2(dm)
print("Mean grads")
print(sum(i0s) / len(i0s))
print(sum(i1s) / len(i1s))
print(sum(i2s) / len(i2s))

