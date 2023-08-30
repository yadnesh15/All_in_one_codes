"""
Created on Aug 04 2021

@author:Yadnesh Kolhe
"""


import os
import pandas as pd
from datetime import datetime
import numpy as np
import pathlib as path
import shutil


# df = r"C:\Users\yadnesh.kolhe\Downloads\DRR"


# output = r"C:\Users\yadnesh.kolhe\Downloads\DRR1"

destination = r"C:\Users\yadnesh.kolhe\Downloads\output/"


source = r"C:\Users\yadnesh.kolhe\Downloads\DRR/"
date_list = pd.date_range(start='2021-01-01', end='2021-06-30')

for item in date_list:
    files_list = os.listdir(source)
    item= item.strftime("%Y-%m-%d")
    for file in files_list:
        if file.__contains__(item):
            print("a")
            dest = destination + "/" + item + "/"
            if os.path.isdir(dest):
                print("Already Present")
            else:
                os.mkdir(dest)
            shutil.move(source + file, dest + file)
        else:
            pass



