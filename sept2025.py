"""
two key assumptions:
- (x1, y1) and (x2, y2) are on opposite sides of the river
- a and b cannot both be zero 
"""

# take in input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a, b, c = map(int, input().split())

# reflect (x1, y1) across ax + by = c
x = x1 - 2*a*(a*x1 + b*y1 - c) / (a**2 + b**2)
y = y1 - 2*b*(a*x1 + b*y1 - c) / (a**2 + b**2)

# calculate distance from (x2, y2) to reflected point (x, y)
print(((y2-y)**2 + (x2-x)**2)**0.5)
