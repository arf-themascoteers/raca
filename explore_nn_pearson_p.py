import evaluate
from ds_manager import DSManager
import torch
from sklearn.metrics import r2_score
from scipy.stats import pearsonr


dm = DSManager("lucas", "hsv")
# r2 = evaluate.r2_once(dm,"nn")
# print(r2)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load("ann.h5")
test_ds = dm.get_test_ds()
x = test_ds.get_x()
x = torch.tensor(x, dtype=torch.float32)
x = x.to(device)
y = test_ds.get_y()
y = torch.tensor(y, dtype=torch.float32)
y = y.to(device)
y = y.reshape(-1,1)
x.requires_grad = True
criterion = torch.nn.MSELoss(reduction='mean')
y_hat = model(x)
loss = criterion(y_hat, y)
loss.backward()
grads = torch.abs(x.grad).sum(axis=0)
grads = (grads/torch.sum(grads))*100
print(grads)

y = y.detach().cpu().reshape(-1)
y_hat = y_hat.detach().cpu().reshape(-1)
pear = pearsonr(y,y_hat)
print(pear.statistic)
print(pear.pvalue)