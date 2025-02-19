'''
essentially just find the maximum amount of fireworks by
each firework launcher in the time period m
e.g: if a = 6 and m = 4, there will be a firework
from minute 0-4, 6-10, etc, meaning there can be at 
max only one firework from launcher a at the same time.
however, if a = 3 and m = 10, there will be a firework 
from minute 0-10, 3-13, 6-16, 9-19, etc, which is a maximum 
of 4 fireworks. this can be found through either
ceiling(m//a) or (m//a)+1. repeat process for other 
firework launcher then just add the two and boom 
'''

n = int(input())
finals = []
for _ in range(n):
    a, b, m = map(int, input().split())
    finals.append((m//a)+1 + (m//b)+1)
for x in finals:
    print(x)
