"""
Created on Aug 04 15:10:13 2021

@author:Yadnesh Kolhe
"""

import os
import pandas as pd
from datetime import datetime,date
import numpy as np
import pathlib as path
import shutil



os.chdir(r"E:\Yadnesh\Global_rms\data\OCFOA\21-09-2021")

# hotel_name = 'OCFOA'
for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)
  

    # # f_y,f_m,f_d = f_name.split("_")[2:]
    # # f_n,f_n2 = f_name.split("/")[:2]
    # file = '{}_{}'.format(hotel_name,)
    # os.rename(f,file)






# for f in os.listdir():
#     f_name,f_ext = os.path.splitext(f)
#     f_y,f_m,f_d = f_name.split("-")[2:]
#     f_n,f_n2 = f_name.split("/")[:2]
#     file = '{}_{}_{}-{}-{}{}'.format(f_n,f_n2,f_y,f_m,f_d,f_ext)
#     os.rename(f,file)
#









# for item in date_list:
#     item = item.strftime("%Y-%m-%d")
#     files_list = os.listdir(source)
#     for file in files_list:
#         f_name, f_ext = os.path.splitext(file)
#         f_y, f_m, f_d = f_name.split("_")[2:]
#         f_n, f_n2 = f_name.split("_")[:2]
#         file = '{}_{}_{}-{}-{}{}'.format(f_n, f_n2, f_y, f_m, f_d, f_ext)
#         if file.__contains__(item):
#             print("a")
#             dest = destination + "/" + item + "/"
#             if os.path.isdir(dest):
#                 print("Already Present")
#             else:
#                 os.mkdir(dest)
#             shutil.move(source + file, dest + file)
#
#         else:
#             pass
#


# files_list = os.listdir(source)
# split_filename = source.split(".")
# os.rename(source,split_filename[:-1] + '_' + '-'.join())