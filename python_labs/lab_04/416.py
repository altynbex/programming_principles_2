import datetime

def parse_date(date: str) -> datetime:
    date_info, time_info, tz = date.split()
    full_date = date_info + " " + time_info
    dt = datetime.datetime.strptime(full_date, "%Y-%m-%d %H:%M:%S")

    sign = 1 if tz[3] == "+" else -1
    hours_offset_from_utc = int(tz[4:6])
    minutes_offset_from_utc = int(tz[7:])
    dt_utc = dt - datetime.timedelta(hours = hours_offset_from_utc, minutes = minutes_offset_from_utc) * sign
    return dt_utc

a = input()
b = input()
d1 = parse_date(a)
d2 = parse_date(b)

print(int(abs(d1 - d2).total_seconds()))