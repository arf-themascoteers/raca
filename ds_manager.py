from lucas_dataset import LucasDataset
from sklearn import model_selection
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import KFold



class DSManager:
    def __init__(self, cspace):
        csv_file_location = f"data_{cspace}.csv"
        df = pd.read_csv(csv_file_location)
        npdf = df.to_numpy()
        npdf = self._normalize(npdf)
        train, test = model_selection.train_test_split(npdf, test_size=0.2, random_state=2)
        self.full_data = np.concatenate((train, test), axis=0)
        self.full_ds = LucasDataset(npdf)
        self.train_ds = LucasDataset(train)
        self.test_ds = LucasDataset(test)

    def get_test_ds(self):
        return self.test_ds

    def get_train_ds(self):
        return self.train_ds

    def get_10_folds(self):
        full_data = self.full_data[0:1000]
        kf = KFold(n_splits=10)
        for i, (train_index, test_index) in enumerate(kf.split(full_data)):
            train_data = full_data[train_index]
            test_data = full_data[test_index]
            yield LucasDataset(train_data), LucasDataset(test_data)

    def get_count_itr(self):
        i = 0
        for train_ds, test_ds in self.get_10_folds():
            i = i+1
        return i

    def _normalize(self, data):
        for i in range(data.shape[1]):
            scaler = MinMaxScaler()
            x_scaled = scaler.fit_transform(data[:,i].reshape(-1, 1))
            data[:,i] = np.squeeze(x_scaled)
        return data


