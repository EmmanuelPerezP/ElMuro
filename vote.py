import datetime
import math


def epoch_seconds(x):
    fecha2 = datetime.datetime(1970, 1, 1)
    diff = x-fecha2
    return diff.total_seconds()


def maximalValue(upvotes, downvotes):
    x = upvotes - downvotes
    z = max(abs(x), 1)
    return z


def score(ups, downs):
    return ups - downs


def hot(ups, downs, date):
    s = score(ups, downs)
    t = epoch_seconds(date)
    order = math.log10(max(abs(s), 1))
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = t - 1134028003
    return round(sign * order + seconds/45000, 7)


time = datetime.datetime(2018, 7, 24, 11, 33)
time2 = datetime.datetime(2018, 7, 25, 19, 33)
print(epoch_seconds(time))
print(epoch_seconds(time2))
print(epoch_seconds(datetime.datetime.now()))

print(hot(10, 0, datetime.datetime.now()))
print(hot(30, 0, datetime.datetime.now()))
print(hot(100, 0, datetime.datetime.now()))
print(hot(1000, 0, datetime.datetime.now()))
print(hot(3000, 0, time2))
