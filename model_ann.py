import torch.nn as nn
import torch.nn.functional as F
import torch


class LucasMachine(nn.Module):
    def __init__(self, size=3, mid=50):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(size, mid),
            nn.LeakyReLU(),
            nn.Linear(mid, 20),
            nn.LeakyReLU(),
            nn.Linear(20, 10),
            nn.LeakyReLU(),
            nn.Linear(10, 1)
        )

    def forward(self, x):
        x = self.fc(x)
        return x

