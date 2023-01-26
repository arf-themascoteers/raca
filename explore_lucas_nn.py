import torch
from train import train
from test import test
import numpy as np
import ds_manager



def calculate_grads(train_ds, test_ds):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_instance = train(device, train_ds)

    x = test_ds.get_x()
    x = torch.tensor(x, dtype=torch.float32)
    x = x.to(device)
    y = test_ds.get_y()
    y = torch.tensor(y, dtype=torch.float32)
    y = y.to(device)
    y = y.reshape(-1, 1)
    x.requires_grad = True
    criterion = torch.nn.MSELoss(reduction='mean')
    y_hat = model_instance(x)
    loss = criterion(y_hat, y)
    loss.backward()
    grads = torch.abs(x.grad).sum(axis=0)
    grads = (grads / torch.sum(grads)) * 100
    return grads[0].item(), grads[1].item(), grads[2].item()

def grads(dm):
    i0s = []
    i1s = []
    i2s = []
    for train_ds, test_ds in dm.get_10_folds():
        i0, i1, i2 = calculate_grads(train_ds, test_ds)
        print(i0, i1, i2)
        i0s.append(i0)
        i1s.append(i1)
        i2s.append(i2)

    return i0s, i1s, i2s


dm = ds_manager.DSManager("lucas", "hsv")
i0s, i1s, i2s = grads(dm)
print("Mean grads")
print(sum(i0s) / len(i0s))
print(sum(i1s) / len(i1s))
print(sum(i2s) / len(i2s))

