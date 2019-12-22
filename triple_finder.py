#!/usr/bin/env python

import math
from functools import partial

a_max = int(input("max a: "))
b_max = int(input("max b: "))
desired_angle = float(input("desired angle: ")*math.pi/180.0)

if a_max < b_max:
    b_max, a_max = a_max, b_max


def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x


def find_triples(a_max, b_max):
    for a in range(1, a_max + 1):
        for b in range(a, b_max + 1):
            c = int(math.sqrt(a*a + b*b) + 0.01)
            if a*a + b*b == c*c:
                yield (a, b, c)


def reduce_triple(triple):
    a, b, c = triple
    divisor = gcd(gcd(a, b), c)
    return (a/divisor, b/divisor, c/divisor)


def angle_diff(desired_angle, triple):
    a, b, c = triple
    angle_a = math.acos(float(a)/float(c))
    angle_b = math.acos(float(b)/float(c))
    return min(abs(desired_angle - angle) for angle in (angle_a, angle_b))


triples = sorted(
    {reduce_triple(triple) for triple in find_triples(a_max, b_max)},
    key=partial(angle_diff, desired_angle)
)

for triple in triples:
    print(triple)
