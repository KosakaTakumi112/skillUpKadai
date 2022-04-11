# coding: utf-8
# Your code here!
import math;

MIN_DEGREE = 0;
MAX_DEGREE = 360;
DEGREE_INTERVAL = 15;

for d in range(MIN_DEGREE,MAX_DEGREE,DEGREE_INTERVAL):
    print(f'sin{d}の値は{math.sin(math.radians(d))}');

for d in range(MIN_DEGREE,MAX_DEGREE,DEGREE_INTERVAL):
    print(f'cos{d}の値は{math.cos(math.radians(d))}');


for d in range(MIN_DEGREE,MAX_DEGREE,DEGREE_INTERVAL):
     print(f'cos{d}の値は{math.cos(math.radians(d))}');
