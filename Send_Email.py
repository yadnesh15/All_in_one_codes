import smtplib
# from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import datetime
today = datetime.datetime.today()
from tabulate import tabulate
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

# creates SMTP session
body = '''Dear Sir/Ma'am,

My interest in the Data Analyst/Engineer position at your organization 
With a strong background in data analysis and a track record of delivering valuable insights, I believe I am well-suited for this role.

Over the past 2.3 years, I have gained extensive experience in the field of data analysis.I possess a deep understanding of extracting data-driven insights,
performing statistical analysis, and utilizing programming languages such as Python and PostgresQL or Advanced Excel. 
I am proficient in tools like PowerBI for data visualization and have hands-on experience with machine learning techniques and time series forecasting.

Beyond my technical skills, I bring industry-specific expertise in the hospitality sector, particularly in revenue management for hotels.
My experience in working with property tax departments in the Government of Maharashtra has also given me a comprehensive understanding of public sector data analysis.

I am excited about the opportunity to apply my skills and knowledge in a dynamic and challenging environment such as yours. I am confident that my technical expertise, 
industry experience, and strong analytical abilities make me a valuable asset to your team.

Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your organization's success.

Serving Notice Period :- Last Day 10th August 2023

Thanks.!

With Regards,
Yadnesh Kolhe

Mobile: +91 
Email:  '''

path = "D:\YK_Code/"
contact_list = pd.read_excel(path + "email_contact.xlsx")


trialmail = [''] #Mail id
for i in contact_list['Contact'].to_list():
# for i in trialmail:
    try:
        ##---------------------------------------------------------------------------------------------------
        # put your email here
        sender = ''
        # get the password in the gmail (manage your google account, click on the avatar on the right)
        # copy the password generated here
        password = ''
        # put the email of the receiver here
        receiver = i
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        rdate1 = datetime.datetime.strftime(today, '%d_%b_%Y')
        message['Subject'] = 'Application of Data Analyst/Engineer' + ' | ' +  'Exp.2.2 Years' + ' | ' + 'Serving Notice Period' + ' | ' + rdate1

        message.attach(MIMEText(body, 'plain'))

        pdfname = 'Yadnesh Kolhe-Data Analyst Resume.pdf'
        # open the file in bynary
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        # payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        # enconding the binary into base64
        encoders.encode_base64(payload)
        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)

        # use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)
        # enable security
        session.starttls()
        # login with mail_id and password
        session.login(sender, password)
        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')

    except:
        pass

