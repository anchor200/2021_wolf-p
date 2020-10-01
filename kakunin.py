#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

dt_now = datetime.now()

presentation = u"""
<html>
<head>
<title>あなたは%sです。</title>
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
あなたは%sです。
<form method="GET" action="./taiki.py">
<input type="submit" value="確認しました"/>
<br><br>
確認ボタンを押した後は、他の人が操作を終えるまでそのままお待ち下さい。<br>
<strong>このページは閉じないでください。</strong>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
<textarea class="textlines" name="Role" readonly>%s</textarea>
</body>
</html>"""

form = cgi.FieldStorage()
keika = form.getvalue('Keika', '')

role = form.getvalue('Role', '')
ro = "村人"
if role == "jinro":
    ro = "人狼"
elif role == "yogen":
    ro = "予言者"

#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation % (ro, ro, keika, ro))

