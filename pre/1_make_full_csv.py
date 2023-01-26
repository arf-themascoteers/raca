import os
import math
import pandas as pd

spectra_file = "spectra.csv"
oc_file = "oc.csv"
out_file = "full.csv"

spectra_df = pd.read_csv(spectra_file)
oc_df = pd.read_csv(oc_file)
out = open(out_file, "w")


spec = 350
while spec <= 2500:
    out.write(f"{spec},")
    spec = spec + 1
out.write("oc")
out.write("\n")

done_ids = []
duplicate_spectra = []
not_found_spectra = []
nans = 0
x = 0
for counter, row in oc_df.iterrows():
    raw_smp_id = row["smp_id"]
    if math.isnan(raw_smp_id):
        nans = nans + 1
        continue
    soc = row["SOC_pred1"]
    if math.isnan(soc):
        continue
    smp_id = int(raw_smp_id)
    if smp_id in done_ids:
        continue

    rows = (spectra_df.loc[spectra_df['smp_id'] == smp_id])

    if len(rows) == 0:
        not_found_spectra.append(smp_id)
        continue
    spectra_row = rows.iloc[0]
    if len(rows) > 1:
        duplicate_spectra.append(spectra_row)

    spec = 350
    while spec <= 2500:
        val = spectra_row[str(spec)]
        out.write(f"{val},")
        spec = spec + 1
    out.write(str(soc))
    out.write("\n")

    done_ids.append(smp_id)
    x = x+1
    if x%100 == 0:
        print("Processed", counter)

print("total",len(done_ids))
print("nans",nans)
print("not found",len(not_found_spectra))
print("duplicate",len(duplicate_spectra))

out.close()
print("done")

