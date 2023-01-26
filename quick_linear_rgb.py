from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import ds_manager


def calculate_r2(train_ds, test_ds):
    train_x = train_ds.get_x()
    train_y = train_ds.get_y()
    test_x = test_ds.get_x()
    test_y = test_ds.get_y()
    model_instance = LinearRegression()
    model_instance = model_instance.fit(train_x, train_y)
    return model_instance.score(test_x, test_y)


dm = ds_manager.DSManager("rgb")
print(calculate_r2(dm.train_ds, dm.test_ds))
