from sklearn.linear_model import LinearRegression
import numpy as np
import ds_manager


def calculate_r2(train_ds, test_ds):
    train_x = train_ds.get_x()
    train_y = train_ds.get_y()
    test_x = test_ds.get_x()
    test_y = test_ds.get_y()
    model_instance = LinearRegression()

    model_instance = model_instance.fit(train_x, train_y)



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


dm = ds_manager.DSManager("rgb")
i0s, i1s, i2s = r2(dm)
print("Mean grads")
print(sum(i0s) / len(i0s))
print(sum(i1s) / len(i1s))
print(sum(i2s) / len(i2s))

