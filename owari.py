#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi
import csv
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

dt_now = datetime.datetime.now()

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
<script>
    function machi() {
        
        $(function(){
          $.ajax({
            url: 'wait2.py',
            type: 'post',
            data: '%s#%s#machi'
          }).done(function(data){
            console.log(data);
            if (data.match(/susumu/)){
                if ('%s' == 'X'){
                    document.getElementById( "tsugi" ).play();
                }
                setTimeout(function(){
<<<<<<< HEAD
                    location.href="http://roboquestion.s3.coreserver.jp/jinro_cn/warihuri.py?room=%s&trial=%s&member=%s";
=======
                    location.href="http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=%s&trial=%s&member=%s";
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
                }, 3*1000);
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
        
        susumu.style.visibility ="hidden";
        machi(); 
    }
</script>
</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
<audio id = "tsugi" src="./tsugi.mp3"></audio>
%s<br><br>

<<<<<<< HEAD
点击了「进⾏下⼀次实验」按钮后，在其他⼈也操作完成前请保持等待。<br>
<button id="susumu" type="button" onclick="OnButtonClick();"/>进⾏下⼀次实验</button>

<br><br>
<strong>请不要关闭⻚⾯。</strong>
=======
「次の実験へ進む」を押した後は、他の人が操作を終えるまでそのままお待ち下さい。<br>
<button id="susumu" type="button" onclick="OnButtonClick();"/>次の実験へ進む</button>

<br><br>
<strong>このページは閉じないでください。</strong>
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
</body>
</html>"""

def wari(str):
    if str == "murabito":
        return "村民"
    elif str == "jinro":
        return "狼人"
    elif str == "yogen":
        return "预⾔家"
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

<<<<<<< HEAD
kekka = "村庄被破坏。"

if Awari == "狼人":
    if Btou == "A" and Ctou == "A":
        kekka = "村⺠胜利了。"
    else:
        kekka = "狼人胜利了。"
elif Bwari == "狼人":
    if Ctou == "B" and Atou == "B":
        kekka = "村⺠胜利了。"
    else:
        kekka = "狼人胜利了。"
elif Cwari == "狼人":
    if Atou == "C" and Btou == "C":
        kekka = "村⺠胜利了。"
    else:
        kekka = "狼人胜利了。"
=======
kekka = "村は滅びました。"

if Awari == "人狼":
    if Btou == "A" and Ctou == "A":
        kekka = "村人の勝利です。"
    else:
        kekka = "人狼の勝利です。"
elif Bwari == "人狼":
    if Ctou == "B" and Atou == "B":
        kekka = "村人の勝利です。"
    else:
        kekka = "人狼の勝利です。"
elif Cwari == "人狼":
    if Atou == "C" and Btou == "C":
        kekka = "村人の勝利です。"
    else:
        kekka = "人狼の勝利です。"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75

room = path.split("./log/")[1].split(".")[0][:-1]

with open("./log/backup/" + dt_now.isoformat() + path.split("./log/")[1].split(".")[0] + ".txt", mode='a') as f:
    f.write("|" + s + "|")

sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
# sys.stdout.write(presentation % (memid, path, memid, room, str(int(exp_num) + 1), memid, Atou, Btou, Ctou, Awari, Bwari, Cwari, form.getvalue('Keika', '')))
sys.stdout.write(presentation % (memid, path, memid, room, str(int(exp_num) + 1), memid, kekka, form.getvalue('Keika', '')))
#sys.stdout.write(presentation)
#sys.stdout.write(s + path)

