import os
import math
import pandas as pd

spectra_file = "spectra.csv"
oc_file = "oc.csv"

spectra_df = pd.read_csv(spectra_file)
oc_df = pd.read_csv(oc_file)

not_found = []
x = 0
for counter, row in spectra_df.iterrows():
    raw_smp_id = row["smp_id"]
    smp_id = int(raw_smp_id)
    rows = (oc_df.loc[oc_df['smp_id'] == smp_id])

    if len(rows) == 0:
        not_found.append(smp_id)
        continue

    x = x+1

print("total",x)
print("not found",len(not_found))
print("done")

