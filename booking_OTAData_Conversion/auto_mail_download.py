
"""
Created on 23 Aug 2019
@author: Swapnil Jiaswal

Upgraded on 16 Oct 2021
@author: Jigar Bhatt
"""

import imaplib
import os
import email
from datetime import date
import datetime
#import send_mail
import pandas as pd
import numpy as np
# import database
import re


email_user = 'revseed@revnomix.com'
email_pass = 'Revenue@123'
imap_url = 'imap.gmail.com'


#attachment_path='E:/Jigar/ftp/email_data'
path='E:/Jigar/ftp/email_data'
# today = datetime.date.today()
# d1 = today.strftime("%Y-%m-%d")
# path = os.path.join(attachment_path, d1)
# if(os.path.exists(path)):
#     print("Allready Exist")
# else:
#     os.mkdir(path)


#map =pd.read_excel(r'C:/ftp/Email_Common_Mapping/Oceanic_mapping_file.xlsx')

def get_sub_file_name( ):
    param_name = 'download'
    db = database.DataBase()
    cnx = db.connect()

    query_hotel = f"select hotel_code from client as ht " \
                  f"inner join " \
                  f"(select client_id, param_value from property_parameters " \
                  f"where param_name = 'download' " \
                  f"and param_value=1) as cc " \
                  f"on (cc.client_id = id);"

    list_a = pd.read_sql(query_hotel, cnx)

    query_sub = f"select source_subject_name, source_file_name" \
                f" from system_source_type " \
                f"where source_system  = 'opera';"
    list_b = pd.read_sql(query_sub, cnx)

    htl_code = list(list_a['hotel_code'].dropna())
    # sub_name_ = list(list_b['source_subject_name'])
    sub_name = list(list_b['source_subject_name'].dropna())
    file_name = list(list_b['source_file_name'].dropna())
    file_name = file_name[0:len(sub_name)]

    sub_list = [str(i + "_" + j) for i in htl_code for j in sub_name]
    file_list = [str(i + "_" + j) for i in htl_code for j in file_name]

    file_dict = dict(zip(sub_list, file_list))
    # for key in list(file_dict.keys()):
    #     subject = re.findall(r"None\b", key)
    #     if len(subject) > 0:
    #         file_dict.pop(key)


    return sub_list, file_list, file_dict


def auth(email_user, email_pass, imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(email_user, email_pass)
    return con
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

def get_attachment(msg,sub,file_list, file_dict):
    test = (msg['Date'])
    # print(test)
    try:
        d = datetime.datetime.strptime(test, '%a, %d %b %Y %H:%M:%S +%f (IST)').strftime('%Y-%m-%d %H:%M:%S')
    except:
        try:
            d = datetime.datetime.strptime(test, '%d %b %Y %H:%M:%S +%f').strftime('%Y-%m-%d %H:%M:%S')
        except:
            d = datetime.datetime.strptime(test, '%a, %d %b %Y %H:%M:%S +%f').strftime('%Y-%m-%d %H:%M:%S')
    # d1 = datetime.datetime.strftime(date.today(),'%Y-%m-%d')

    db = database.DataBase()
    cnx = db.connect()

    hotel_code, file_type = (file_dict.get(sub)).split('_',1)
    query_date = f"select max(extraction_date) as exd from data_status " \
                  f"where file_type like '{file_type}%' and " \
                  f"hotel_code = '{hotel_code}'"

    d1 = pd.read_sql(query_date, cnx)
    d1 = str(d1['exd'][0])
    # print(d)
    # print(d1)



    if (d > d1):
        for part in msg.walk():
            if part.get_content_maintype()=="multipart":
                continue
            fileName = part.get_filename()
            fileType = part.get_content_type()
            if bool(fileName):
                if fileName in file_list:
                    filePath = os.path.join(path, fileName)
                    with open(filePath,'wb') as f:
                        f.write(part.get_payload(decode=True))
                        print('{} file downloaded successfully'.format(fileName))
                        # fl_name = sub
                        # map['Status'] = np.where(map['Hotel Name'] == fl_name, 'Success', map['Status'])
                elif fileType == 'file/txt':
                    file_name_reqd = file_dict.get(sub)
                    fileName = fileName.replace(fileName, file_name_reqd)
                    filePath = os.path.join(path, fileName)
                    with open(filePath, 'wb') as f:
                        f.write(part.get_payload(decode=True))
                        print('{} file downloaded successfully'.format(fileName))
                        # fl_name = sub
                        # map['Status'] = np.where(map['Hotel Name'] == fl_name, 'Success', map['Status'])

    else:
        pass
        # fl_name = sub
        # map['Status'] = np.where(map['Hotel Name'] == fl_name, 'Failed', map['Status'])
        # ema_name = dict(zip(map['Hotel Name'], map['Email Id']))
        # email_id = ema_name[fl_name]
        # send_mail.send_alert_msg(fl_name, "missing on", d1, email_id)

def emailAttachment():
    sub_list, file_list, file_dict = get_sub_file_name()
    con = auth(email_user,email_pass,imap_url)

    #con.select('INBOX')
    con.select('"[Gmail]/All Mail"')

    # weekday = datetime.date.today().strftime('%A')
    # print(weekday)

    # sub_list = ["SFONV_Res_Statistics_MST", "SFONV_Res_Forecast_MST",
    #             "SFONV_Res_Statistics_RMT", "SFONV_Res_Forecast_RMT",
    #
    #             "SBAZS History & Forecast", "SBAZS_Res_Statistics_MST", "SBAZS_Res_Forecast_MST",
    #             "SBAZS_Res_Statistics_RMT", "SBAZS_Res_Forecast_RMT"]

    for sub in sub_list:
        result, data =con.uid('search',None,'SUBJECT "{}"'.format(sub))
        inbox_item_list=data[0].split()
        item = sorted(inbox_item_list, reverse=True)
        if len(item) == 0:
            continue
        else:
            item = item[0]

        result2, email_data = con.uid('fetch',item,'(RFC822)')
        raw_email = email_data[0][1].decode('utf-8')

        # for item in inbox_item_list:                                 # commented and moved out of loop J.B. 29Sept'2021
        #     result2, email_data = con.uid('fetch',item,'(RFC822)')
        #     raw_email = email_data[0][1].decode('utf-8')

        email_message = email.message_from_string(raw_email)
        # t =(email_message['Date'])
        # print(t)
        get_attachment(email_message,sub,file_list, file_dict)
    #map.to_excel(r'C:/ftp/Email_Common_Mapping/Oceanic_mapping_file.xlsx', index=False)
    con.logout()

if __name__ =='__main__':
    emailAttachment()
