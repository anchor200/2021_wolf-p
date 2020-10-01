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
この村には人狼がいると思いますか？<br>

<form method="GET" action="./taiki.py">
<input type="submit" name="Jinro" value="いる"/>
<input type="submit" name="Jinro" value="いない"/>
<br><br>
<strong>このページは閉じないでください。</strong>
</body>
</html>"""

form = cgi.FieldStorage()



#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation)

