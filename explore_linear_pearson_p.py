from sklearn.linear_model import LinearRegression
import numpy as np
import ds_manager
from scipy.stats import pearsonr


def calculate_r2(train_ds, test_ds):
    train_x = train_ds.get_x()
    train_y = train_ds.get_y()
    test_x = test_ds.get_x()
    test_y = test_ds.get_y()
    model_instance = LinearRegression()

    model_instance = model_instance.fit(train_x, train_y)
    y_hat = model_instance.predict(test_x)
    pear = pearsonr(test_y, y_hat)
    return pear.statistic, pear.pvalue


def r2(dm):
    ss = []
    ps = []
    for train_ds, test_ds in dm.get_10_folds():
        s,p = calculate_r2(train_ds, test_ds)
        ss.append(s)
        ps.append(p)

    return ss, ps


dm = ds_manager.DSManager("lucas", "hsv")
ss, ps = r2(dm)
print("Mean grads")
print(sum(ss) / len(ss))
print(sum(ps) / len(ps))

