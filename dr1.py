import os
import pandas as pd
from datetime import datetime
import numpy as np
import pathlib as path
import shutil

source = r"C:\Users\yadnesh.kolhe\Downloads\DRR/"

files_list = os.listdir(source)

# for file in os.listdir(source):
# 	os.rename(file, f"{file}_")






# split_filename = source.split(".")
# os.rename(source,split_filename[:-1] + '_' + '-'.join())
#
for fn in files_list:
    parts = (fn.split("_")[2:])
    newname = fn[0] + "-".join(parts)
    os.rename(fn,newname)