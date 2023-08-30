import pandas as pd
from datetime import datetime,timedelta
from pathlib import Path
import os
import csv

def process_trafford(data,mapfile,checkFile):


    data["Total Rooms"] = data["Total Occ. "] + data["Blocked "]

    cols = mapfile["key"]
    df = pd.DataFrame(data,columns=cols)

    for check in checkFile["Invalid_Data"]:
        idx = df[df['Date ']== check].index
        df.drop(idx, inplace=True)

    df = df.sort_values(['Date '])
    # Dropping NA idf column Total Rooms contains NA
    df = df.dropna(how='all')
    df['Date ']= pd.to_datetime(df["Date "], format = "%d/%m/%Y %a ")
    df['Date ']=df['Date '].dt.strftime('%d %B %Y')


    df["Total Rooms"] = df["Total Occ. "] + df["Blocked "]


    ren_dict =dict(zip(mapfile.key,mapfile.Values))
    df.rename(columns=ren_dict,inplace=True)

    df.drop(['Total Occ. ','Blocked '],axis= 'columns', inplace=True)

    return df
if __name__=="__main__":
    today = datetime.today().date()
    filename = 'Hotel_Statistics'
    std_path = r"E:/Yadnesh/Trafford/"
    in_path = std_path + "\Input/" + str(today)
    outpath = std_path + "\Output/" + str(today)
    map_path = std_path + "\Mapping/"

    mapfile = pd.read_excel(map_path + "\map_col.xlsx")
    data = pd.read_excel(in_path + "/" + "Hotel_Statistics.xlsx", skiprows=10, usecols="D:AA")
    checkFile = pd.read_excel(map_path + "\check_values.xlsx")

    final_df = process_trafford(data,mapfile,checkFile)
    if os.path.isdir(outpath):
        print(filename + " " + "Data is already Present")
    else:
        os.mkdir(outpath)
    final_df.to_csv(outpath + "\Trafford_HNF.txt",sep='|',index=False)
    print("Trafford_HNF is Dumped Successfull")
else:
    print("Data file is not Found")

