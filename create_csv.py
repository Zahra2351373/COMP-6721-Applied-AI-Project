import os
import pandas as pd

DIR = "../UTKFace"
files = os.listdir(DIR)

df = pd.DataFrame(columns=["filename","age","gender","race"])

for file in files:
    attributes = file.split("_")
    if len(attributes) == 4:
        df.loc[-1] = [file,attributes[0],attributes[1],attributes[2]]
        df.index = df.index + 1
        df = df.sort_index()
    
df.to_csv("UTKFace_sample.csv", index=False)
