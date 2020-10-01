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

<script type="text/javascript">

    function OnButtonClick_iru() {
        iru.style.visibility ="hidden";
        inai.style.visibility ="hidden";
        uketsuke.style.visibility ="visible";
        taiki_iru();
         
    }
    function OnButtonClick_inai() {
        iru.style.visibility ="hidden";
        inai.style.visibility ="hidden";
        uketsuke.style.visibility ="visible";
        taiki_inai();

    }
    function taiki_iru(){
        $(function(){
          $.ajax({
            url: 'kakikomi2.py',
            type: 'post',
            data: '%s#%s#iru'
          }).done(function(data){
            console.log(data);
            if (data.match(/pending/)){
                console.log("calling again");
                taiki_iru();
                console.log("called");
            }
            else if (data.match(/done/)){
                console.log(data);
                tsugi.style.visibility ="visible";
            }
            else{
                console.log("calling again on rewirte");
                taiki_iru();
                console.log("called");
            
            }
          });
        });
    }
    
    function taiki_inai(){
        $(function(){
          $.ajax({
            url: 'kakikomi2.py',
            type: 'post',
            data: '%s#%s#inai'
          }).done(function(data){
            console.log(data);
            if (data.match(/pending/)){
                console.log("calling again");
                taiki_inai();
                console.log("called");
            }
            else if (data.match(/done/)){
                console.log(data);
                tsugi.style.visibility ="visible";
            }
            else{
                console.log("calling again on rewirte");
                taiki_inai();
                console.log("called");
            
            }
          });
        }); 
    }
    
    
</script>

</head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" /> </head>
<body>
<p id="iruka">この村には人狼がいると思いますか？</p><br>
<p id="uketsuke">投票を受け付けました。他の人が投票を終えると、この下に「次へ」ボタンが出ます。出たらクリックしてください。</p><br>

<form method="GET" action="./Tohyo2.py">
<input id="iru" type="button" value="いる" onclick="OnButtonClick_iru();"/>
<input id="inai" type="button" value="いない" onclick="OnButtonClick_inai();"/>
<br>
<input id="tsugi" type="submit" value="次へ"/><br>
<br><br>
<strong>このページは閉じないでください。一度投票した後で戻るボタンを押してしまった場合は、ページを更新してください。</strong>
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
            url: 'kakikomi2.py',
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
<p id="iruka">あなたはすでに投票しています。</p><br>
<p id="uketsuke">投票を受け付けました。他の人が投票を終えると、この下に「次へ」ボタンが出ます。出たらクリックしてください。</p><br>

<form method="GET" action="./Tohyo2.py">
<input id="koushingo" type="button" value="ページを更新してしまった場合はこのボタンを押してください。" onclick="OnButtonKoushin();"/>
<br>
<input id="tsugi" type="submit" value="次へ"/><br>
<br><br>
<strong>このページは閉じないでください。一度投票した後で戻るボタンを押してしまった場合は、ページを更新してください。</strong>
<script type="text/javascript">
document.getElementById("tsugi").style.visibility ="hidden";
document.getElementById("uketsuke").style.visibility ="visible";
document.getElementById("iruka").style.visibility ="visible";
document.getElementById("koushingo").style.visibility ="visible";
</script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<textarea class="textlines" name="Keika" readonly>%s</textarea>
</body>
</html>"""

form = cgi.FieldStorage()

memid = form.getvalue('Keika', '').split("#")[0]
path = form.getvalue('Keika', '').split("#")[-1]
with open(path) as f:
    s = f.read()
if ("Tohyo2:A" in s and memid == "A") or ("Tohyo2:B" in s and memid == "B") or ("Tohyo2:C" in s and memid == "C"):
    # print("Content-type: text/html;charset=utf-8\n")
    sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
    sys.stdout.write(presentation_uketsuketa % (memid, path, form.getvalue('Keika', '')))

else:
    #print("Content-type: text/html;charset=utf-8\n")
    sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
    sys.stdout.write(presentation % (memid, path, memid, path, form.getvalue('Keika', '')))

