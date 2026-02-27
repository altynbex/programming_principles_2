x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

"""
let A = (x1, y1)
B' = (x2, -y2)

B'- A = (x2 - x1, -y2 - y1)

x = x1 + s(x2 - x1)
y = y1 + s(-y2 - y1), as Yr (reflection point) = 0 -> 0 = y1-s(y2 + y1) -> x = y1 / (y2 + y1)

x = x1 + (x2 - x1) * y1 / (y2 + y1)
"""


answer = x1 + (x2 - x1) * y1 / (y2 + y1)
print(f"{answer:.10f} 0.0000000000")