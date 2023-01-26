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
    return model_instance.score(test_x, test_y)


def r2(dm):
    r2s = []
    for train_ds, test_ds in dm.get_10_folds():
        r2 = calculate_r2(train_ds, test_ds)
        print(r2)
        r2s.append(r2)

    return np.array(r2s)


if __name__ == "__main__":
    dm = ds_manager.DSManager("hsv")
    ar = r2(dm)
    result = sum(ar)/len(ar)
    print("Result", result)

