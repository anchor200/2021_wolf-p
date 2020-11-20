#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

recieve = sys.stdin.readline()

print('Content-type: text/html\n')
with open(recieve.split('#')[1]) as f:
    s = f.read()

if "koushingo" not in recieve:
    if recieve.split('#')[0] + ":1" not in s:
        with open(recieve.split('#')[1], mode='a') as f:
            f.write(recieve.split('#')[0] + ":1")

if "hajimetai" in recieve:
    if recieve.split('#')[0] == "X" and "A:1" in s and "B:1" in s and "C:1" in s and "X:1" not in s:
        print("hajimaru")
    """if recieve.split('#')[0] == "A" and "X:1" in s and "B:1" in s and "C:1" in s and "A:1" not in s:
        print("hajimaru")
    elif recieve.split('#')[0] == "B" and "X:1" in s and "C:1" in s and "A:1" in s and "B:1" not in s:
        print("hajimaru")
    elif recieve.split('#')[0] == "C" and "X:1" in s and "A:1" in s and "B:1" in s and "C:1" not in s:
        print("hajimaru")
    elif recieve.split('#')[0] == "X" and "A:1" in s and "B:1" in s and "C:1" in s and "X:1" not in s:
        print("hajimaru")"""
else:
    if "owaru" in recieve:
        with open(recieve.split('#')[1], mode='a') as f:
            f.write("owatta")

    if "owarimachi" not in recieve:
        t = 0
        snapped = False
        while True:
            t += 1
            with open(recieve.split('#')[1]) as f:
                s = f.read()
            if "owatta" in s:
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
            print("owatta")

    else:
        t = 0
        snapped = False
        while True:
            t += 1
            with open(recieve.split('#')[1]) as f:
                s = f.read()
            if "A:1" in s and "B:1" in s and "C:1" in s and "X:1" in s:
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
            print(recieve)