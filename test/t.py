#!/usr/bin/env python3
import sys
from math import *
from collections import defaultdict
from queue import deque  # Queues
from heapq import heappush, heappop  # Priority Queues

# parse
lines = [line.strip() for line in sys.stdin.readlines()]
u, v = list(map(int, lines[0].split()))


def f(u, v):
    if u > v:
        return None
    if u == 0 and v == 0:
        return []
    if u == v:
        return [u]
    y = v - u
    z = y // 2
    if y % 2 == 0:
        if (u + z) ^ z == u:
            return [u + z, z]
        else:
            return [u, z, z]
    return None


xs = f(u, v)
if xs is None:
    print(-1)
else:
    print(len(xs))
    if xs:
        print(' '.join(map(str, xs)))