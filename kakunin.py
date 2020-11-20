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
<<<<<<< HEAD
        return "村民"
    elif str == "jinro":
        return "狼人"
    elif str == "yogen":
        return "预⾔家"
=======
        return "村人"
    elif str == "jinro":
        return "人狼"
    elif str == "yogen":
        return "予言者"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
    else:
        return "エラーを起こせし者"


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

dt_now = datetime.now()

presentation = u"""
<html>
<head>
<title>你是%s。</title>
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
<<<<<<< HEAD
<font color="#0000ff" size="6">你是%s。</font><br>
%s
<form id="next" method="GET" action="./taiki.py">
<br><br>
按了确定按钮后，请等待其他⼈操作完成。<br>
<button id="kakunin" type="button" onclick="OnButtonClick();"/>确定</button>
<br><strong>请不要关闭这个⽹⻚。</strong>
=======
<font color="#0000ff" size="6">あなたは%sです。</font><br>
%s
<form id="next" method="GET" action="./taiki.py">
<br><br>
確認ボタンを押した後は、他の人が操作を終えるまでそのままお待ち下さい。<br>
<button id="kakunin" type="button" onclick="OnButtonClick();"/>確認しました</button>
<br><strong>このページは閉じないでください。</strong>
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
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
<<<<<<< HEAD
            yogen = "你是预⾔家，你的占⼘结果，B是" + Bwari + "。"
        if memid == "B":
            yogen = "你是预⾔家，你的占⼘结果，C是" + Cwari + "。"
        if memid == "C":
            yogen = "你是预⾔家，你的占⼘结果，A是" + Awari + "。"
    else:
        if memid == "A":
            yogen = "你是预⾔家，你的占⼘结果，C是" + Cwari + "。"
        if memid == "B":
            yogen = "你是预⾔家，你的占⼘结果，A是" + Awari + "。"
        if memid == "C":
            yogen = "你是预⾔家，你的占⼘结果，B是" + Bwari + "。"
=======
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
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75





<<<<<<< HEAD
ro = "村民"
=======
ro = "村人"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
if role == "jinro":
    ro = "狼人"
elif role == "yogen":
<<<<<<< HEAD
    ro = "预⾔家"
=======
    ro = "予言者"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
elif role == "experimenter":
    ro = "実験者"

#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
sys.stdout.write(presentation % (ro, memid, path, ro, yogen, keika, ro))


