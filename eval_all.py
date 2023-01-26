import numpy as np
import pandas as pd
import ds_manager
import evaluate
import os


def process():
    columns = {"linear" : "Linear", "plsr": "PLSR","rf" : "RF", "svr": "SVR", "nn" : "NN"}
    params = [
        "rgb",
        "hsv",
        "hsv_xy",
        "XYZ",
        "xyY",
        "cielab"
    ]
    data = np.zeros((len(params), len(columns)))
    column_values = [columns[key] for key in columns.keys()]
    names = [par for par in params]

    path = f"results.csv"

    if os.path.exists(path):
        df = pd.read_csv(path)
        df.drop(columns=df.columns[0], axis=1, inplace=True)
        part_data = df.to_numpy()
        data[0:part_data.shape[0], 0:part_data.shape[1]] = part_data

    for index_par, par in enumerate(params):
        for index_col, col in enumerate(columns):
            print("Start",f"{col} - {par}")
            if data[index_par][index_col] != 0:
                print("Was done already: ", data[index_par][index_col])
            else:
                ds = ds_manager.DSManager(par)
                r2s = evaluate.r2(ds, col)
                r2_mean = np.mean(r2s)
                print(par, col, r2_mean)
                r2_log = open(f"log.txt", "a")
                r2_log.write(f"{col} - {par}: {str(r2s)}\n")
                r2_log.close()
                data[index_par][index_col] = r2_mean
                df = pd.DataFrame(data=data, columns=column_values, index=names)
                df.to_csv(path)

    print("Done all")


if __name__ == "__main__":
    process()