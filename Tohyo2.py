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

presentation_SomeJinro = u"""
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

<script type="text/javascript">

    function OnButtonClick_Jin1() {
        Jin1.style.visibility ="hidden";
        Jin2.style.visibility ="hidden";
        uketsuke.style.visibility ="visible";
        taiki_Jin1();
    }
    function OnButtonClick_Jin2() {
        Jin1.style.visibility ="hidden";
        Jin2.style.visibility ="hidden";
        uketsuke.style.visibility ="visible";
        taiki_Jin2();
    }
    
    function taiki_Jin1(){
        $(function(){
          $.ajax({
            url: 'kakikomi3.py',
            type: 'post',
            data: '%s#%s#%s'
          }).done(function(data){
            console.log(data);
            if (data.match(/pending/)){
                console.log("calling again");
                taiki_Jin1();
                console.log("called");
            }
            else if (data.match(/done/)){
                console.log(data);
                tsugi.style.visibility ="visible";
            }
            else{
                console.log("calling again on rewirte");
                taiki_Jin1();
                console.log("called");
            
            }
            
          });
        });
    }
    
    function taiki_Jin2(){
        $(function(){
          $.ajax({
            url: 'kakikomi3.py',
            type: 'post',
            data: '%s#%s#%s'
          }).done(function(data){
            console.log(data);
            if (data.match(/pending/)){
                console.log("calling again");
                taiki_Jin2();
                console.log("called");
            }
            else if (data.match(/done/)){
                console.log(data);
                tsugi.style.visibility ="visible";
            }
            else{
                console.log("calling again on rewirte");
                taiki_Jin2();
                console.log("called");
            
            }
          });
        }); 
    }
    
</script>

</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
<<<<<<< HEAD
<p id="dareka">你认为谁是狼⼈？</p><br>
%s
<p id="uketsuke">我们接收到了你的投票。在其他⼈也都投票完成之后，下⾯会出现「下⼀步」的按钮。按钮出现之 后，请点击按钮。</p><br>
=======
<p id="dareka">誰が人狼だと思いますか？</p><br>
%s
<p id="uketsuke">投票を受け付けました。他の人が投票を終えると、この下に「次へ」ボタンが出ます。出たらクリックしてください。</p><br>
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75

<form method="GET" action="./owari.py">
<input id="Jin1" type="button" value="%s" onclick="OnButtonClick_Jin1();"/>
<input id="Jin2" type="button" value="%s" onclick="OnButtonClick_Jin2();"/>
<br>
<input id="tsugi" type="submit" value="下⼀步"/><br>
<br><br>
<strong>请不要关闭这个⻚⾯。如果你在投票后按了返回键，请更新⻚⾯。</strong><br>
如果你是按 "返回 "键来到了这个⻚⾯，请不要按上⾯的按钮，按浏览器的 "前进 “键返回原界⾯， 刷新⻚⾯。
<script type="text/javascript">
document.getElementById("tsugi").style.visibility ="hidden";
document.getElementById("uketsuke").style.visibility ="hidden";
</script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
</body>
</html>"""

presentation_uketsuketa = u"""
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
<script type="text/javascript">
    
    function OnButtonKoushin(){
        koushingo.style.visibility ="hidden";
        $(function(){
          $.ajax({
            url: 'kakikomi3.py',
            type: 'post',
            data: '%s#%s#koushingo'
          }).done(function(data){
            console.log(data);
            if (data.match(/pending/)){
                console.log("calling again");
                OnButtonKoushin();
                console.log("called");
            }
            else if (data.match(/done/)){
                console.log(data);
                tsugi.style.visibility ="visible";
            }
            else{
                console.log("calling again on rewirte");
                OnButtonKoushin();
                console.log("called");
            
            }
          });
        });
    }
</script>

</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
<p id="dareka">你已经投了票。</p><br>
<p id="uketsuke">我们接收到了你的投票。在其他⼈也都投票完成之后，下⾯会出现「下⼀步」的按钮。按钮出现之 后，请点击按钮。。</p><br>
<input id="koushingo" type="button" value="如果你已经刷新了页面，请按这个按钮。" onclick="OnButtonKoushin();"/>

<form method="GET" action="./owari.py">
<br>
<input id="tsugi" type="submit" value="下⼀步"/><br>
<br><br>
<strong>请不要关闭⻚⾯。</strong>
<script type="text/javascript">
document.getElementById("tsugi").style.visibility ="hidden";
document.getElementById("uketsuke").style.visibility ="visible";
document.getElementById("dareka").style.visibility ="visible";
</script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
</body>
</html>"""


presentation_NoJinro = u"""
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
%s<br>
<br>


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

jikken = ""
if memid == "X":
    jikken = "実験者にだけ見えている文章：実験者の投票は結果に影響しません。適当に押してください"

if "Tohyo2:A:inai" in s and "Tohyo2:B:inai" in s and "Tohyo2:C:inai" in s:
    presentation = presentation_NoJinro
    # print("Content-type: text/html;charset=utf-8\n")

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
    kekka = "村民胜利了"
    if Awari == "狼人" or Bwari == "狼人" or Cwari == "狼人":
        # kekka = "村庄被破坏"
        kekka = "狼⼈胜利了"
=======
    kekka = "村人の勝利です。"
    if Awari == "人狼" or Bwari == "人狼" or Cwari == "人狼":
        # kekka = "村は滅びました。"
        kekka = "人狼の勝利です。"
>>>>>>> 57d794743891e1d34848594caa378c7e48308e75


    with open("./log/backup/" + dt_now.isoformat() + path.split("./log/")[1].split(".")[0] + ".txt", mode='a') as f:
        f.write("|" + s + "|")
    room = path.split("./log/")[1].split(".")[0][:-1]
    sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
    sys.stdout.write(presentation % (memid, path, memid, room, str(int(exp_num) + 1), memid, kekka, form.getvalue('Keika', '')))
elif ("Tohyo3:A" in s and memid == "A") or ("Tohyo3:B" in s and memid == "B") or ("Tohyo3:C" in s and memid == "C"):
    presentation = presentation_uketsuketa
    sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
    sys.stdout.write(presentation % (memid, path, form.getvalue('Keika', '')))
else:
    presentation = presentation_SomeJinro
    p1 = "人物γ"
    p2 = "人物γ"
    pp1 = ""
    pp2 = ""
    if memid == "A":
        p1 = "人物B"
        p2 = "人物C"
        pp1 = "Jinro=B"
        pp2 = "Jinro=C"
    elif memid == "B":
        p1 = "人物C"
        p2 = "人物A"
        pp1 = "Jinro=C"
        pp2 = "Jinro=A"
    elif memid == "C":
        p1 = "人物A"
        p2 = "人物B"
        pp1 = "Jinro=A"
        pp2 = "Jinro=B"

    sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
    sys.stdout.write(presentation % (memid, path, pp1, memid, path, pp2, jikken, p1, p2, form.getvalue('Keika', '')))






