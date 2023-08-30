import numpy as np
import pandas as pd

from datetime import datetime, date, timedelta

df = pd.read_excel("E:\Yadnesh\Demo TaskFile/demo.xlsx")
today = datetime.today()

df["Modified Date"] = df["Date/ Time Booked (GMT)"] + timedelta(days = 1)

df["Modified Date"] = np.where(df["Modified Date"] < today,
                               np.where(df["Modified Date"]<=df["CheckIn Date"],
                                 np.where(df["Status"] != "Confirmed",
                                    df["Modified Date"], df["Date/ Time Booked (GMT)"]),
                                    df["Date/ Time Booked (GMT)"]),df["Date/ Time Booked (GMT)"])

# df["Modified Date"] = np.where((df["Modified Date"]< today) and
#                                (df["Status"].any() in ["Cancelled", "Modified"]), df["Modified Date"], df["Date/ Time Booked (GMT)"])

# df["Modified Date"] = np.where(df["Status"] == "Cancelled",
#                     df["Modified Date"],
#                                df["Date/ Time Booked (GMT)"])
# df["Check"] = df["Date/ Time Booked (GMT)"]

df.to_excel("E:\Yadnesh\Demo TaskFile/demo_ct1.xlsx")

