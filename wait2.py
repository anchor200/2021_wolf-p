#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

recieve = sys.stdin.readline()

print('Content-type: text/html\n')
with open(recieve.split('#')[1]) as f:
    s = f.read()

if recieve.split('#')[0] + ":4" not in s:
    with open(recieve.split('#')[1], mode='a') as f:
        f.write(recieve.split('#')[0] + ":4")

t = 0
snapped = False
while True:
    t += 1
    with open(recieve.split('#')[1]) as f:
        s = f.read()
    if "A:4" in s and "B:4" in s and "C:4" in s and "X:4" in s:
        break
    time.sleep(0.2)

    if t >= 1000:
        snapped = True
        break

if snapped:
    print("pending")
else:
    recieve = recieve + "OK!"
    recieve += s
    print("susumu")