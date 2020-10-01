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
<title>あなたは人狼です。</title>
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
あなたは人狼です。
<form method="GET" action="/giron_zenhan.py">
<input type="submit" value="確認しました"/>
</body>
</html>"""

form = cgi.FieldStorage()



#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation)

