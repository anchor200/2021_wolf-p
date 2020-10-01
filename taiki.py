#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import random
import sys
import io
import cgi
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

dt_now = datetime.now()
presentation = u"""
<html>
<head>
<title>ボタンを押して議論を開始してください。</title>
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
            
            
                var huga = 1;
                var hoge = setInterval(function() {
                    console.log(huga);
                    huga++;
                    //終了条件
                    if (huga == 30) {
                        document.getElementById( "naka" ).play();
                    }
                    if (huga == 60) {
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
        document.getElementById( "hajime" ).play();
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

<audio id = "hajime" src="./kaishi.mp3"></audio>
<audio id = "naka" src="./naka.mp3"></audio>
<audio id = "owari" src="./owari.mp3"></audio>

<p id="inst1">あなたは%sです。<br><br>下のボタンを押して議論に進んでください。<br>
制限時間は三分です。<br><br></p>
<p id="inst2">今すぐZoomに戻って議論を行ってください。<br></p>
<p id="inst3">下のボタンを押して投票に進んでください。<br></p>
<input id="hajimeBut" type="button" value="確認して議論を開始する(このボタンを必ず押してください)" onclick="OnButtonClick();"/>

<form method="GET" action="./Tohyo1.py">
<input id="owariBut" type="submit" value="確認して投票に移る"/><br>
<strong>このページを閉じたり、戻るや進むを押さないでください。</strong><br>
投票画面から戻るを押してこのページに来てしまった場合は、上のボタンは押さず、ブラウザの進むを押して投票画面に戻り、ページを更新してください。

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


while True:
    with open(path) as f:
        s = f.read()
    if "A:0" in s and "B:0" in s and "C:0" in s:
        break
    time.sleep(0.2)

#print("Content-type: text/html;charset=utf-8\n")
sys.stdout.write('Content-type: text/html; charset=UTF-8\n\n')
#sys.stdout.write(presentation)
sys.stdout.write(presentation % (memid, path, memid, path, memid, path, role, form.getvalue('Keika', '')))

