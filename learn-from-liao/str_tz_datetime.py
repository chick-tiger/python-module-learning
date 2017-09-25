import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    t = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'UTC(.)(\d{1,2}):00', tz_str)
    if tz.group(1) == '+':
	    tz_num = int(tz.group(2))
    else:
	    tz_num = -int(tz.group(2))
    t = t.replace(tzinfo=timezone(timedelta(hours=tz_num)))
    stamp_t = t.timestamp()
    return stamp_t
	
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print(t2)
print('Pass')
