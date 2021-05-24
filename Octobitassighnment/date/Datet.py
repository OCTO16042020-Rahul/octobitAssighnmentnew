# _author_='Rahul kharatmol'

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('Yesterday date : ',yesterday)
print('Today date : ',today)
print('Tomorrow date  : ',tomorrow)
