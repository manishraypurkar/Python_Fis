import datetime
print("Date before adding:\n",datetime.datetime.strftime(datetime.date.today(),"%d/%m/%y"))
print("Date after adding:\n",datetime.datetime.strftime(datetime.date.today()+datetime.timedelta(days=10),"%d/%m/%y"))
