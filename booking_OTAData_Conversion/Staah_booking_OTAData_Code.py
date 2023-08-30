"""
Importing all libraries required
"""
import pandas as pd
import numpy as np
import os
from datetime import datetime,date,timedelta
from pathlib import Path
from zipfile import ZipFile
import warnings
warnings.filterwarnings('ignore')

"""
        This code converts the OTA data of Staah_max property into Staah property OTA data format which will then passed on Revseed
         The output file name will be as "Staah_booking_OTAData_htlcode".
        
        :param stdpath: The standard folder path, it will be the Parent folder
        :param in_path: Input file path
        :param map_path will be the 
        :param mapping: utility mapping file
        :param mapfile: In mapping Folder to read map_col file
       

"""

# infile = in_path + "{}_OTA Data".format(htlname)


def process_staahmax(htlcode,infile,mapfile):
    """

    :param htlcode: The hotel Code for which Data to be converted / the property id
    :param infile: The input File name
    :param mapfile:
    :return:
    """
    Staah_data = pd.read_excel(infile,skiprows=2)
    mapfile =pd.read_excel(mapfile)

    # To Create the dictionary of col_name used for col_rename of Staah_data

    ren_dict =dict(zip(mapfile.before,mapfile.after))
    Staah_data = pd.DataFrame(Staah_data,columns=mapfile.before.to_list())

    Staah_data.rename(columns=ren_dict,inplace=True)

    Staah_data["Net Amount"] = Staah_data["Total Amount"]

# In Room type column separate the Specific values include ","

    Staah_data['Room Type'] = Staah_data['Room Type'].str.split(",").str[0]

# To Check and Drop NAN or Na Values
    Staah_data.dropna(subset=['Channel'], inplace=True)

# converting the Date columns in datetime format.

    try:
        Staah_data['Date/ Time Booked (GMT)'] = pd.to_datetime(Staah_data['Date/ Time Booked (GMT)'],
                                                               format='%d-%b-%Y %I:%M:%S %p (IST)')
    except:
        Staah_data['Date/ Time Booked (GMT)'] = pd.to_datetime(Staah_data['Date/ Time Booked (GMT)'],
                                                               format='%d-%b-%Y %I:%M:%S %p')
# Converting the Date Dtype in to datetime format.

    Staah_data["CheckIn Date"]=pd.to_datetime(Staah_data["CheckIn Date"])

    Staah_data["Date/ Time Modified (GMT)"] = Staah_data["Date/ Time Booked (GMT)"] + timedelta(days = 1)
    today = datetime.today()
    Staah_data["Date/ Time Modified (GMT)"] = np.where(Staah_data["Date/ Time Modified (GMT)"] < today,
                                                       np.where(Staah_data["Date/ Time Modified (GMT)"] <= Staah_data["CheckIn Date"],
                                                                np.where(Staah_data["Status"] != "Confirmed",
                                                                         Staah_data["Date/ Time Modified (GMT)"],Staah_data["Date/ Time Booked (GMT)"]),
                                                                         Staah_data["Date/ Time Booked (GMT)"]),Staah_data["Date/ Time Booked (GMT)"])

#  Again, Converting the Modified & CheckIn Date column in DD-MM-YYYY

    Staah_data["Date/ Time Modified (GMT)"] = pd.to_datetime( Staah_data["Date/ Time Modified (GMT)"]).dt.strftime('%d %b %Y')
    Staah_data["CheckIn Date"] = pd.to_datetime(Staah_data["CheckIn Date"]).dt.strftime('%d %b %Y')

    try:
        Staah_data['Date/ Time Booked (GMT)'] = pd.to_datetime(Staah_data['Date/ Time Booked (GMT)'],
                                                               format='%d-%b-%Y %I:%M:%S %p (IST)').dt.strftime('%d %b %Y')
    except:
        Staah_data['Date/ Time Booked (GMT)'] = pd.to_datetime(Staah_data['Date/ Time Booked (GMT)'],
                                                               format='%d-%b-%Y %I:%M:%S %p').dt.strftime('%d %b %Y')

    Staah_data['Property Id'] = htlcode

    
    return Staah_data

if __name__ == '__main__':

    today = datetime.today().date()
    # htlname = "Rhythm"
    # htlname = "Breathing Earth"
    # htlcode = 2568
    # htlcode = 9462

  
    std_path = r"E:/Yadnesh/Staah Max/"
    in_path = std_path + "Input/"
    outpath = std_path +  "\Output/" + str(today)
    map_path = std_path + "\Mapping/"
    mapfile = map_path + "\map_col.xlsx"


    if os.path.isdir(in_path):
        files = os.listdir(in_path)
        if len(files) > 0 :
            if files[0].__contains__("Booking"):
                infile = in_path + "/" + files[0]
                htlcode= (infile.split("_")[-1]).split(".")[0]
                fin_data = process_staahmax(htlcode, infile, mapfile)
                if os.path.isdir(outpath):
                    print("Already Present")
                else:
                    os.mkdir(outpath)
                fin_data.to_csv(outpath + "\Staah_booking_OTAData_{}.csv".format(htlcode), index=False)
                # sp = os.path.join(infile)
                # tp = os.path.join(file_path, f'{infile}.archived')
                # os.replace(sp, tp)
                print(htlcode + " data is dumped")
            else:
                print("No Booking Data found")
        else:
            print("No Booking Data found")
    else:
        print("({})'s s booking data folder not found".format(today))
        # exit()
