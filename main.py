import yagmail
import pandas
import openpyxl
from News import NewsFeed
import datetime


df = pandas.read_excel("news_users.xlsx")
date = datetime.datetime.now()-datetime.timedelta(days=1)
date= date.strftime('%Y-%m-%d')

for index,row in df.iterrows():
    nf = NewsFeed(interest=row['Interest'], from_date= date,to_date=date)
    print(nf.get())
    email = "pythontestproject86@gmail.com"
    password = "python$123"
    new_password= "tuxdszvkblialapl"

    email = yagmail.SMTP(user = email, password= new_password)

    email.send(to = row['Email'] , subject= f"Your {row['Interest']} news for today!" ,
               contents= f"Hi {row['Name']}!, \n  See what's on about {row['Interest']} today. \n {nf.get()}")



"""
 email = "pythontestproject86@gmail.com"
    password = "python$123"
    new_password= "tuxdszvkblialapl"

    email = yagmail.SMTP(user = email, password= new_password)

    email.send(to = "siddharthk04025@gmail.com" , subject= "Hi There <EOM>" ,
               contents= "Test Email. Ignore me.",
               attachments= "Design.txt")
"""
#class Email:

