#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

dt_now = datetime.now()

presentation = u"""
<html>
<head>
<title>三人人狼</title>
<style>
.textlines {
    border: 0px solid #fff;  /* 枠線 */
    border-radius:0em;   /* 角丸 */
    padding: 0em;          /* 内側の余白量 */
    background-color: snow;  /* 背景色 */
    width:0em;             /* 横幅 */
    height: 0px;           /* 高さ */
}
</style>
</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
Aさんは%sさんが人狼だと言いました。<br>
Bさんは%sさんが人狼だと言いました。<br>
Cさんは%sさんが人狼だと言いました。<br><br>

Aさんは%sです。<br>
Bさんは%sです。<br>
Cさんは%sです。<br><br>


<a href="http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=testroom&trial=%s&member=%s">次の実験へ進む</a>

<br><br>
<strong>このページは閉じないでください。</strong>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
</body>
</html>"""

def wari(str):
    if str == "murabito":
        return "村人"
    elif str == "jinro":
        return "人狼"
    elif str == "yogen":
        return "予言者"
    else:
        return "エラーを起こせし者"


form = cgi.FieldStorage()

memid = form.getvalue('Keika', '').split("#")[0]
path = form.getvalue('Keika', '').split("#")[-1]
with open(path) as f:
    s = f.read()

Apos = s.index('Tohyo3:A:Jinro=')
Atou = s[Apos + len("Tohyo3:A:Jinro=")]
Bpos = s.index('Tohyo3:B:Jinro=')
Btou = s[Bpos + len("Tohyo3:B:Jinro=")]
Cpos = s.index('Tohyo3:C:Jinro=')
Ctou = s[Cpos + len("Tohyo3:C:Jinro=")]

Awari = ""
Bwari = ""
Cwari = ""
with open("warihuri.csv") as f:
    exp_num = ""
    for row in csv.reader(f):
        if row[0] + row[1] == path.split("./log/")[1].split(".")[0]:
            exp_num = row[1]
            Awari = wari(row[2])
            Bwari = wari(row[3])
            Cwari = wari(row[4])


with open("./log/backup/" + path.split("./log/")[1].split(".")[0] + ".txt") as f:
    f.write(s)

sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation % (Atou, Btou, Ctou, Awari, Bwari, Cwari, str(int(exp_num) + 1), memid, form.getvalue('Keika', '')))



