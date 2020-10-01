# wolf-p
## アクセス方法
### リンク
http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?

### ?以降の指定方法
room=”グループID”
trial=”実験ID”
member=”人物”
人物はA, B, Cで指定

例<br>
http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=testroom&trial=0&member=A
http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=testroom&trial=0&member=B
http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=testroom&trial=0&member=C

途中で問題が発生した場合は、memberをCLEARと指定しアクセスする。こうすることでログが抹消される。<strong>(取り扱い注意)</strong>
ログを抹消しないと再度リンクにアクセスしても正しく動作しない。

例
http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?room=testroom&trial=0&member=CLEAR

## 実験の作成方法
サーバーにwarihuri.csvをアップロードする。現在テスト用は以下のファイル。
http://roboquestion.s3.coreserver.jp/jinro/warihuri.csv



## 実験ごとのログ
http://roboquestion.s3.coreserver.jp/jinro/testroom0.txt
jinro/以下は、[グループID][実験ID].txt

このファイルをダウンロードすると、被験者が選んだ選択肢がわかる (データ分析用)

## 各ページの説明
最初の画面
<img width="669" alt="スクリーンショット 2020-10-02 2 02 53" src="https://user-images.githubusercontent.com/32958889/94840438-65b3a200-0453-11eb-8ce6-591be0a40e4e.png">

次の画面。被験者の役割が表示される。
<img width="670" alt="スクリーンショット 2020-10-02 2 03 15" src="https://user-images.githubusercontent.com/32958889/94840490-73692780-0453-11eb-89e7-3abcc118390d.png">

全員が[確認しました]を押すと次の画面に遷移する。
<img width="644" alt="スクリーンショット 2020-10-02 2 03 49" src="https://user-images.githubusercontent.com/32958889/94840613-a14e6c00-0453-11eb-8291-135e42080317.png">

[確認して議論を開始する]を押すと以下の画面に遷移する。「zoomに戻ってマイクとカメラをオンにして議論してください」という音声が流れる。この時点ではタイマーは起動しない。全員が[確認して議論を開始する]を押すとタイマーが起動する。
<img width="670" alt="スクリーンショット 2020-10-02 2 03 57" src="https://user-images.githubusercontent.com/32958889/94840619-a6132000-0453-11eb-88f0-55fe479164f8.png">

タイマーが制限時間一分前になると、「終了一分前です」という音声が流れる。終了時間になると「マイクとカメラをオフにして投票してください」という音声が流れる。
このとき、最大で5秒ラグがある(原因が分かれば修正します)。
最後に[確認して議論を開始する]を押した人のブラウザからのみ音声が流れる。
ブラウザがミュートになっていないか注意する。
音声が流れると、[確認して投票に移る]ボタンが表示される。
<img width="669" alt="スクリーンショット 2020-10-02 2 04 01" src="https://user-images.githubusercontent.com/32958889/94840625-aad7d400-0453-11eb-9d23-6535caae08af.png">

投票画面　全員が人狼がいないと言った場合はここで終わり
<img width="669" alt="スクリーンショット 2020-10-02 2 04 06" src="https://user-images.githubusercontent.com/32958889/94840637-b0351e80-0453-11eb-9a10-7318272f2b71.png">

投票をしたあとで更新ボタンを押してしまった場合には以下のボタンが出る。
<img width="669" alt="スクリーンショット 2020-10-02 2 04 10" src="https://user-images.githubusercontent.com/32958889/94840642-b4f9d280-0453-11eb-8f83-c700259a2bdb.png">

結果発表(勝敗表示は作成中です)
<img width="671" alt="スクリーンショット 2020-10-02 2 04 14" src="https://user-images.githubusercontent.com/32958889/94840657-b925f000-0453-11eb-87a6-b194193575f4.png">

