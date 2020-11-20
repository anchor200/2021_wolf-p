#!/usr/bin/env python3
# coding: utf-8
import csv
from datetime import datetime
import random
import sys
import io
import cgi
import time

from datetime import datetime

with open('warihuri.csv', "a") as f:
    writer = csv.writer(f)
    writer.writerow(["room","trial","A","B","C"])

for i in range(1000):
    for j in range(5):
        room = "room" + str(i)
        trial = j
        warihuri = []
        if random.random() <= 0.6:
            if random.choice([0,1]):
                warihuri = ["murabito", "murabito", "jinro"]
            else:
                warihuri = ["murabito", "yogen", "jinro"]
        else:
            if random.choice([0,1]):
                warihuri = ["murabito", "murabito", "murabito"]
            else:
                warihuri = ["murabito", "yogen", "murabito"]
        random.shuffle(warihuri)

        with open('warihuri.csv', "a") as f:
            writer = csv.writer(f)
            writer.writerow([room, trial] + warihuri)