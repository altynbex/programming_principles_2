a = int(input())
b = list()
d = dict()
for i in range(a):
    dorama_name, dorama_series_amount_str = map(str, input().split())
    dorama_series_amount_int = int(dorama_series_amount_str)
    try:
        d[dorama_name] += dorama_series_amount_int
    except KeyError:
        d[dorama_name] = 0
        d[dorama_name] += dorama_series_amount_int

sorted_d = sorted(d)

for k in sorted_d:
    print(k, d[k])