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
<p id="dareka">誰が人狼だと思いますか？</p><br>
<p id="uketsuke">投票を受け付けました。他の人が投票を終えると、この下に「次へ」ボタンが出ます。出たらクリックしてください。</p><br>

<form method="GET" action="./owari.py">
<input id="Jin1" type="button" value="%s" onclick="OnButtonClick_Jin1();"/>
<input id="Jin2" type="button" value="%s" onclick="OnButtonClick_Jin2();"/>
<br>
<input id="tsugi" type="submit" value="次へ"/><br>
<br><br>
<strong>このページは閉じないでください。一度投票した後で戻るボタンを押してしまった場合は、ページを更新してください。</strong><br>
戻るを押してこのページに来てしまった場合は、上のボタンは押さず、ブラウザの進むを押してもとの画面に戻り、ページを更新してください。
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
<p id="dareka">あなたはすでに投票しています。</p><br>
<p id="uketsuke">投票を受け付けました。他の人が投票を終えると、この下に「次へ」ボタンが出ます。出たらクリックしてください。</p><br>
<input id="koushingo" type="button" value="ページを更新してしまった場合はこのボタンを押してください。" onclick="OnButtonKoushin();"/>

<form method="GET" action="./owari.py">
<br>
<input id="tsugi" type="submit" value="次へ"/><br>
<br><br>
<strong>このページは閉じないでください。</strong>
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
</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
全会一致で人狼がいないことになりました<br>
<br>

Aさんは%sです。<br>
Bさんは%sです。<br>
Cさんは%sです。<br><br>


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


if "Tohyo2:A:inai" in s and "Tohyo2:B:inai" in s and "Tohyo2:C:inai" in s:
    presentation = presentation_NoJinro
    # print("Content-type: text/html;charset=utf-8\n")

    Awari = ""
    Bwari = ""
    Cwari = ""
    with open("warihuri.csv") as f:
        for row in csv.reader(f):
            if row[0] + row[1] == path.split("./")[1].split(".")[0]:
                Awari = wari(row[2])
                Bwari = wari(row[3])
                Cwari = wari(row[4])

    sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
    sys.stdout.write(presentation % (Awari, Bwari, Cwari, form.getvalue('Keika', '')))
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
    sys.stdout.write(presentation % (memid, path, pp1, memid, path, pp2, p1, p2, form.getvalue('Keika', '')))






