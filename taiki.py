#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi
import time
import csv

def wari(str):
    if str == "murabito":
<<<<<<< HEAD
        return "村民"
    elif str == "jinro":
        return "狼人"
    elif str == "yogen":
        return "预⾔家"
    else:
        return "エラーを起こせし者"

=======
        return "村人"
    elif str == "jinro":
        return "人狼"
    elif str == "yogen":
        return "予言者"
    else:
        return "エラーを起こせし者"


>>>>>>> 57d794743891e1d34848594caa378c7e48308e75

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

dt_now = datetime.now()
presentation = u"""
<html>
<head>
<title>请按下下⾯的按钮进⾏讨论。</title>
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

<script type="text/javascript">
    function sleep(waitSec, callbackFunc) {
      var spanedSec = 0;
     
      var waitFunc = function () {
     
          spanedSec++;
     
          if (spanedSec >= waitSec) {
              if (callbackFunc) callbackFunc();
              return;
          }
     
          clearTimeout(id);
          id = setTimeout(waitFunc, 1000);
      
      };
      var id = setTimeout(waitFunc, 1000); 
    }
    
    function machi() {
        
        $(function(){
          $.ajax({
            url: 'kakikomi.py',
            type: 'post',
            data: '%s#%s#owarimachi'
          }).done(function(data){
            console.log(data);
            if (data.match(/owatta/)){
                owariBut.style.visibility ="visible";
                inst1.style.visibility ="hidden";
                inst2.style.visibility ="hidden";
                inst3.style.visibility ="visible";
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
    function Hajime() {
        
        $(function(){
          $.ajax({
            url: 'kakikomi.py',
            type: 'post',
            data: '%s#%s#hajimetai'
          }).done(function(data){
            console.log(data);
            if (data.match(/hajimaru/)){
            
                document.getElementById( "hajime" ).play();
                var huga = 1;
                var hoge = setInterval(function() {
                    console.log(huga);
                    huga++;
                    //終了条件
                    if (huga == 120) {
                        document.getElementById( "naka" ).play();
                    }
                    if (huga == 180) {
                        clearInterval(hoge);
                        document.getElementById( "owari" ).play();
                        $(function(){
                          $.ajax({
                            url: 'kakikomi.py',
                            type: 'post',
                            data: '%s#%s#owaru'
                          }).done(function(data){
                            console.log(data);        
                          });
                        });
                        owariBut.style.visibility ="visible";
                        inst1.style.visibility ="hidden";
                        inst2.style.visibility ="hidden";
                        inst3.style.visibility ="visible";
                    }
                }, 1000);
                                  
            } 
            else {
                console.log("calling machi");
                machi();
      
            }

          });
        });
        
        return false;
    }
    
    function OnButtonClick(){
        
        hajimeBut.style.visibility ="hidden";
        inst1.style.visibility ="hidden";
        inst2.style.visibility ="visible";
        inst3.style.visibility ="hidden";
        Hajime(); 
    }

    
</script>

</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>

<audio id = "hajime" src="./hajime.mp3"></audio>
<audio id = "naka" src="./tochu.mp3"></audio>
<audio id = "owari" src="./saigo.mp3"></audio>
<<<<<<< HEAD
<br><font color="#0000ff" size="6">你是%s。<br></font>%s<br><br>
<p id="inst1">请按下下⾯的按钮进⾏讨论。<br>

限制时间为三分钟。<br><br></p>
<p id="inst2">请在听到语⾳播报后，返回zoom界⾯，开始讨论。<br></p>
<p id="inst3">点击下面的按钮，继续进行投票。<br></p>
=======
<br><font color="#0000ff" size="6">あなたは%sです。<br></font>%s<br><br>
<p id="inst1">下のボタンを押して議論に進んでください。<br>

制限時間は三分です。<br><br></p>
<p id="inst2">音声アナウンスが流れたら、zoomの画面に移動して議論を開始してください。<br></p>
<p id="inst3">下のボタンを押して投票に進んでください。<br></p>
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
<button id="hajimeBut" type="button" onclick="OnButtonClick();"/>%s</button>

<form method="GET" action="./Tohyo1.py">
<input id="owariBut" type="submit" value="确定进⼊投票⻚⾯ "/><br>
<strong>请不要关闭此⽹⻚，也不要点击前进或后退按钮。 </strong><br>
如果是从投票⻚⾯按了返回键回到了这个⻚⾯的情况，请不要按上述确定的按钮，请点击浏览器的 前进键，返回投票⻚⾯，更新⽹⻚。 


<script type="text/javascript">
document.getElementById("owariBut").style.visibility ="hidden";
document.getElementById("inst2").style.visibility ="hidden";
document.getElementById("inst3").style.visibility ="hidden";
</script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
</body>
</html>"""


form = cgi.FieldStorage()
memid = form.getvalue('Keika', '').split("#")[0]
path = form.getvalue('Keika', '').split("#")[-1]
role = form.getvalue('Role', '')
with open(path, mode='a') as f:
    f.write(memid + ":0")
with open(path) as f:
    s = f.read()
<<<<<<< HEAD
buttonstr = "确定开始讨论（请务必按下这个按钮）<br>在按下按钮后，请等待语⾳播报。 请在听到语⾳播报后，进⼊ZOOM界⾯，开始讨论。 "
=======
buttonstr = "確認して議論を開始する(このボタンを必ず押してください。<br>ボタンを押した後は音声アナウンスがあるまでお待ち下さい。音声アナウンスが流れたら、zoomの画面に移動して議論を開始してください)"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
if memid == "X":
    buttonstr = "実験者専用ボタン：確認して議論を開始する(このボタンを必ず押してください)"

if "A:1" in s and "B:1" in s and "C:1" in s and "X:1" in s:
<<<<<<< HEAD
    buttonstr = "由于操作错误，页面已被刷新。 如果讨论还没有结束，请务必按这个按钮返回讨论。<br>如果实验者已经更新，请重启会话。"
=======
    buttonstr = "操作ミスによりページが更新されました。議論がまだ終わっていない場合はこのボタンを必ず押して議論に戻ってください。<br>実験者が更新してしまった場合はセッションをリスタートしてください。"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75


while True:
    with open(path) as f:
        s = f.read()
    if "A:0" in s and "B:0" in s and "C:0" in s and "X:0" in s:
        break
    time.sleep(0.2)

if memid == "X":
    while True:
        with open(path) as f:
            s = f.read()
        if "A:1" in s and "B:1" in s and "C:1" in s:
            break
        time.sleep(0.2)



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
<<<<<<< HEAD
if role == "yogen":
=======
if role == "予言者":
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75
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


#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
#sys.stdout.write(presentation)
sys.stdout.write(presentation % (memid, path, memid, path, memid, path, role, yogen, buttonstr, form.getvalue('Keika', '')))

