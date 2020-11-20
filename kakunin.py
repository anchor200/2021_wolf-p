#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi
import random
import csv


def wari(str):
    if str == "murabito":
        return "村人"
    elif str == "jinro":
        return "人狼"
    elif str == "yogen":
        return "予言者"
    else:
        return "エラーを起こせし者"


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
<script>
    function machi() {
        
        $(function(){
          $.ajax({
            url: 'wait.py',
            type: 'post',
            data: '%s#%s#machi'
          }).done(function(data){
            console.log(data);
            if (data.match(/susumu/)){
                document.getElementById("next").submit();
            } 
            else {
                console.log("calling again");
                machi();
                console.log("called");
            }

          });
        });
        
        return false;
    }
    
    function OnButtonClick(){
        
        kakunin.style.visibility ="hidden";
        machi(); 
    }
</script>
</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
<font color="#0000ff" size="6">あなたは%sです。</font><br>
%s
<form id="next" method="GET" action="./taiki.py">
<br><br>
確認ボタンを押した後は、他の人が操作を終えるまでそのままお待ち下さい。<br>
<button id="kakunin" type="button" onclick="OnButtonClick();"/>確認しました</button>
<br><strong>このページは閉じないでください。</strong>
<script>
document.getElementById("owariBut").style.visibility ="hidden";
</script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
<textarea class="textlines" name="Role" readonly>%s</textarea>
</body>
</html>"""

form = cgi.FieldStorage()
keika = form.getvalue('Keika', '')
memid = form.getvalue('Keika', '').split("#")[0]
path = form.getvalue('Keika', '').split("#")[-1]
role = form.getvalue('Role', '')

Awari = ""
Bwari = ""
Cwari = ""
with open("warihuri.csv") as f:
    for row in csv.reader(f):
        if row[0] + row[1] == path.split("./log/")[1].split(".")[0]:
            Awari = wari(row[2])
            Bwari = wari(row[3])
            Cwari = wari(row[4])
yogen = ""
if role == "yogen":
    random.seed(path.split("./log/")[1].split(".")[0])
    co = random.choice([0, 1])
    if co:
        if memid == "A":
            yogen = "あなたの占いの結果、Bさんは" + Bwari + "だとわかりました。"
        if memid == "B":
            yogen = "あなたの占いの結果、Cさんは" + Cwari + "だとわかりました。"
        if memid == "C":
            yogen = "あなたの占いの結果、Aさんは" + Awari + "だとわかりました。"
    else:
        if memid == "A":
            yogen = "あなたの占いの結果、Cさんは" + Cwari + "だとわかりました。"
        if memid == "B":
            yogen = "あなたの占いの結果、Aさんは" + Awari + "だとわかりました。"
        if memid == "C":
            yogen = "あなたの占いの結果、Bさんは" + Bwari + "だとわかりました。"





ro = "村人"
if role == "jinro":
    ro = "人狼"
elif role == "yogen":
    ro = "予言者"
elif role == "experimenter":
    ro = "実験者"

#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation % (ro, memid, path, ro, yogen, keika, ro))


