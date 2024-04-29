import os
import random
import shutil

DIR = "./UTKFace"
files = os.listdir(DIR)

print(len(files))

selected = random.sample(files, 10000)

for file in selected:
    shutil.copy2(DIR+"/"+file,"./sampled/"+file)