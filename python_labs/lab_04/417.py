import math

R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
b = 2 * (x1 * dx + y1 * dy)
c = x1 * x1 + y1 * y1 - R*R

D = b * b - 4 * a * c

segment_length = math.sqrt(a)

if D < 0:
    if x1*x1 + y1*y1 <= R*R and x2*x2 + y2*y2 <= R:
        print(f"{segment_length:.10f}")
    else:
        print("0.0000000000")
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2 * a)
    t2 = (- b + sqrtD) / (2 * a)
    
    t_min = min(t1, t2)
    t_max = max(t1, t2)

    left = max(0.0, t_min)
    right = min(1.0, t_max)

    if left > right:
        if x1*x1 + y1*y1 <= R*R and x2*x2 + y2*y2 <= R:
            print(f"{segment_length:.10f}")
        else:
            print("0.0000000000")
    else:
        answer = (right - left) * segment_length
        print(f"{answer:.10f}")