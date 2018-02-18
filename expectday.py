# This is a snippet for finding the day .
# INPUT FORMAT  : Date Month Year
# OUTPUT FORMAT : Weekname

import calendar
d,m,y=map(int,input().split())
print((calendar.day_name[calendar.weekday(y,m,d)]).upper())





