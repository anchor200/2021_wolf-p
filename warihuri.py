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
你是⼈物%s吗？
<form method="GET" action="./kakunin.py">
<input type="submit" value="是"/>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
<textarea class="textlines" name="Role" readonly>%s</textarea>

%s
</body>
</html>"""


presentation_kanri = u"""
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
<form method="GET" action="./clear.py">
<input type="submit" value="%sのログをクリアする(取り扱い注意)"/>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
<textarea class="textlines" name="Role" readonly>%s</textarea>

</body>
</html>"""

presentation_otsu = u"""
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
<<<<<<< HEAD
实验就到此为止。 谢谢你的帮助。<br>
<strong>此后，按照实验者的指示进行。</strong>
=======
実験は以上です。お疲れさまでした。<br>
<strong>以後は実験者の指示に従ってください。</strong>
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
<textarea class="textlines" name="Keika" readonly>%s</textarea>
<textarea class="textlines" name="Role" readonly>%s</textarea>

</body>
</html>"""


form = cgi.FieldStorage()
if ("room" in form) and ("trial" in form) and ("member" in form):
    s1 = "エラー"
    s2 = "warihuri"
    with open("warihuri.csv") as f:
        for row in csv.reader(f):
            if form["member"].value == "CLEAR":
                s1 = "CLEAR"
                s2 = "ファイルをクリア"
                break
            if row[0] == form["room"].value and row[1] == form["trial"].value:
                s1 = form["member"].value
                if s1 == "A":
                    s2 = row[2]
                if s1 == "B":
                    s2 = row[3]
                if s1 == "C":
                    s2 = row[4]
                if s1 == "CLEAR":
                    s2 = "ファイルをクリア"
                if s1 == "X":
                    s2 = "experimenter"


else:
    s1 = "エラー"
    s2 = "warihuri"

path = "./log/" + form["room"].value + form["trial"].value + ".txt"
try:
    with open(path, mode='x') as f:
        f.write("last created " + dt_now.isoformat())
except FileExistsError:
    pass


jikkensya = ""
if s1 == "X":
    with open(path) as f:
        s = f.read()
    if len(s) >= 45:
        jikkensya = "<br><strong>実験者にだけ見えている文章： " + path +" のログがクリアされていないと思われます。確認してください。<br>ログをクリアしたら、更新してこの文章が消えるか確認してください。<br>ログをクリアしたら、被験者の方に、「あなたは人物Mですか？」という画面に一度戻ってもらってから再開してください。</strong><br>"

# ファイルをクリアする
if s1 == "CLEAR":
    presentation = presentation_kanri % (form["room"].value + form["trial"].value, s1 + "#" + path, s2)
else:
    presentation = presentation % (s1, s1 + "#" + path, s2, jikkensya)

if s1 == "エラー":
    presentation = presentation_otsu % (s1 + "#" + path, s2)



#presentation = presentation % (s1, s1 + "#" + path, s2)

#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation)

#http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=testroom&trial=0&member=A
