#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi
import time

from datetime import datetime
dt_now = datetime.now()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

form = cgi.FieldStorage()
path = form.getvalue('Keika', '').split("#")[-1]

with open(path, mode='w') as f:
    f.write("last cleared " + dt_now.isoformat())

sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write("cleared")
