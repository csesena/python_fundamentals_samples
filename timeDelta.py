from datetime import datetime

def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    difference = dt1 - dt2

    return str(abs(int(difference.total_seconds())))


print(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
