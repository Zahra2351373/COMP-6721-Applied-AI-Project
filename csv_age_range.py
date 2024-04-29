import pandas as pd

DIR = "./UTKFace"

data = pd.read_csv('UTKFace.csv', index_col=False, usecols=["gender","race","age"])

def age_group(age):
    if age >=0 and age < 18:
        return 1
    elif age < 30:
        return 2
    elif age < 80:
        return 3
    else:
        return 4
    
data["age_range"] = data.apply(lambda row: age_group(row.age), axis=1)

data.to_csv("UTKFace_with_age_range.csv", index=False)