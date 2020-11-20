#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

recieve = sys.stdin.readline()

print('Content-type: text/html\n')
print(recieve + "read OK!")
print("writing: " + recieve.split('#')[1] + "||" + "@Tohyo3:" + recieve.split('#')[0] + ":" + (
        recieve.split('#')[-1]))
print(recieve.split('#'))


if "koushingo" not in recieve:
    print("koushingo deha nai")
    with open(recieve.split('#')[1]) as f:
        s = f.read()
    if "Tohyo3:" + recieve.split('#')[0] + ":" not in s:
        with open(recieve.split('#')[1], mode='a') as f:
            f.write("@Tohyo3:" + recieve.split('#')[0] + ":" + (recieve.split('#')[-1]))

print(recieve + "write OK!")

t = 0
snapped = False
while True:
    t += 1
    with open(recieve.split('#')[1]) as f:
        s = f.read()
    if "Tohyo3:A" in s and "Tohyo3:B" in s and "Tohyo3:C" in s and "Tohyo3:X" in s:
        break
    time.sleep(0.2)

    if t >= 100:
        snapped = True
        break

if snapped:
    print("pending")
else:
    recieve = recieve + "OK!"
    print("done")