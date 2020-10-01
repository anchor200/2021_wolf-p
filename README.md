# wolf-p
## アクセス方法
### リンク
http://roboquestion.s3.coreserver.jp/jinro/warihuri.py?

### ?以降の指定方法
room=”グループID”
trial=”実験ID”
member=”人物”
人物はA, B, Cで指定

例
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

次の画面。被験者の役割が表示される。


全員が[確認しました]を押すと次の画面に遷移する。


[確認して議論を開始する]を押すと以下の画面に遷移する。「zoomに戻ってマイクとカメラをオンにして議論してください」という音声が流れる。この時点ではタイマーは起動しない。全員が[確認して議論を開始する]を押すとタイマーが起動する。

タイマーが制限時間一分前になると、「終了一分前です」という音声が流れる。終了時間になると「マイクとカメラをオフにして投票してください」という音声が流れる。
このとき、最大で5秒ラグがある(原因が分かれば修正します)。
最後に[確認して議論を開始する]を押した人のブラウザからのみ音声が流れる。
ブラウザがミュートになっていないか注意する。
音声が流れると、[確認して投票に移る]ボタンが表示される。


投票画面　全員が人狼がいないと言った場合はここで終わり


投票をしたあとで更新ボタンを押してしまった場合には以下のボタンが出る。


結果発表(勝敗表示は作成中です)


