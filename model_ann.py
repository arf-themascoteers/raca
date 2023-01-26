import torch.nn as nn
import torch.nn.functional as F
import torch


class LucasMachine(nn.Module):
    def __init__(self, size=3, mid=10):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(size, mid),
            nn.LeakyReLU(),
            nn.Linear(mid, 5),
            nn.LeakyReLU(),
            nn.Linear(5, 1)
        )

    def forward(self, x):
        x = self.fc(x)
        return x

