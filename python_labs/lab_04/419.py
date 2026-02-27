import math
r = int(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dA = math.sqrt(x1*x1 + y1*y1)
dB = math.sqrt(x2*x2 + y2*y2)


direct = math.hypot(x2-x1, y2-y1)
cross = abs(x1*y2 - x2*y1) / direct

# vector AB
dx = x2 - x1
dy = y2 - y1

# projection parameter
t = -(x1*dx + y1*dy) / (dx*dx + dy*dy)

if 0 <= t <= 1:
    # closest point lies on segment
    closest_x = x1 + t*dx
    closest_y = y1 + t*dy
    dist_to_center = math.hypot(closest_x, closest_y)
else:
    # closest point is one of the endpoints
    dist_to_center = min(dA, dB)

if dist_to_center >= r:
    print(f"{direct:.10f}")
else:
    alpha = math.acos(r / dA)
    beta = math.acos(r / dB)

    at1 = math.sqrt(dA**2 - r**2)
    t2b = math.sqrt(dB**2 - r**2)

    theta = math.acos((x1*x2 + y1*y2) / (dA * dB))

    answer = at1 + t2b + r * (theta - alpha - beta)

    print(f"{answer:.10f}")


# if cross >= r:
#     print(f"{direct:.10f}")
# else:
#     alpha = math.acos(r / dA)
#     beta = math.acos(r / dB)

#     at1 = math.sqrt(dA**2 - r**2)
#     t2b = math.sqrt(dB**2 - r**2)

#     theta = math.acos((x1*x2 + y1*y2) / (dA * dB))

#     answer = at1 + t2b + r * (theta - alpha - beta)
#     print(f"{answer:.10f}")