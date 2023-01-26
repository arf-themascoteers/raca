import torch
from train import train
from test import test
import ds_manager
import numpy as np


def calculate_r2(train_ds, test_ds):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_instance = train(device, train_ds)
    return test(device, test_ds, model_instance)


dm = ds_manager.DSManager("hsv_xy")
print(calculate_r2(dm.train_ds, dm.test_ds))

