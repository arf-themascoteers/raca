import evaluate
from ds_manager import DSManager
import torch
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

dm = DSManager("lucas", "hsv")

model_instance = LinearRegression()
model_instance = model_instance.fit(dm.get_train_ds().get_x()[:,0:1], dm.get_train_ds().get_y())
r2 = model_instance.score(dm.get_test_ds().get_x()[:,0:1], dm.get_test_ds().get_y())
print("Hue",r2)

model_instance = LinearRegression()
model_instance = model_instance.fit(dm.get_train_ds().get_x()[:,1:2], dm.get_train_ds().get_y())
r2 = model_instance.score(dm.get_test_ds().get_x()[:,1:2], dm.get_test_ds().get_y())
print("Value",r2)

model_instance = LinearRegression()
model_instance = model_instance.fit(dm.get_train_ds().get_x()[:,2:3], dm.get_train_ds().get_y())
r2 = model_instance.score(dm.get_test_ds().get_x()[:,2:3], dm.get_test_ds().get_y())
print("Saturation",r2)