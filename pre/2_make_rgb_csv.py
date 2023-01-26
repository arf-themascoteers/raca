import pandas as pd

out_file = "full.csv"
rgb_file = "rgb.csv"

out_df = pd.read_csv(out_file)
cols = [str(i) for i in range(350, 2501) if i not in [490, 560, 665]]
out_df.drop(columns=cols, axis=1, inplace=True)
out_df = out_df.loc[:, ["665", "560", "490", "oc"]]
out_df.columns = ["r", "g", "b", "oc"]
out_df.to_csv(rgb_file, index=False)

print("Done")
