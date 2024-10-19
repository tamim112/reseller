import datetime
import urllib
db = DAL('mysql://root:@localhost/master', decode_credentials=True)
date_fixed=datetime.datetime.now()#+datetime.timedelta(hours=6)

#format
date_format                         = "%Y-%m-%d"
clock_12_format                     = "%I:%M %p"
clock_24_format                     = "%H:%M:%S"
date_time_24_format                 = "%Y-%m-%d %H:%M:%S"
date_time_12_format                 = "%Y-%m-%d %I:%M %p"

#valueWithformat
current_date                        = date_fixed.strftime(date_format)
current_time_24_format              = date_fixed.strftime(clock_24_format)
current_time_12_format              = date_fixed.strftime(clock_12_format)
current_date_time_24_format         = date_fixed.strftime(date_time_24_format)
current_date_time_12_format         = date_fixed.strftime(date_time_12_format)

cur_year = date_fixed.strftime("%Y")
cur_month = date_fixed.strftime("%m")
cur_date = date_fixed.strftime("%d")