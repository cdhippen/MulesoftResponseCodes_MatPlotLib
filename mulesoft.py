import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import drange, date2num
import datetime

date1 = datetime.datetime(2018, 1, 24, 1, 45, 00)
date2 = datetime.datetime(2018, 2, 10, 7, 20, 00)
delta = datetime.timedelta(seconds=1)
dates = drange(date1, date2, delta)
status_codes = []
datetimes = []
dates2 = []

for match in re.finditer(r'\[(\d{4}(?:-\d{2}){2})(?:\s'
                         r'(?P<time>(?:\d+:){2}[^.]+).*'
                         r'Response code (?P<code>\d+))?',
                         open('log.log', 'r').read()):
    if match.group('time'):
        datetimes.append(str(match.group(1) + ' ' +
                         str(match.group('time'))))
        status_codes.append(str(match.group('code')))
        with open('succinctlog.log', 'a') as f:
            f.write(str(match.group(1, 'time', 'code')))
            f.write('\n')

for i in datetimes:
    x = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
    x = date2num(x)
    dates2.append(x)

y = np.array(status_codes)
x = np.array(dates2)
plt.plot_date(x, y)
