## これはなに

Linux初学者向け講座の講師⽤メモです。Ubuntu版。Linuxほぼ触ったことがない⼈向け。これを終えると以下ができるようになります。

* Linuxのディレクトリ構造の理解
* ファイルエクスプローラー操作
* テキストエディタの操作
* パーミッションの概念の理解
* sudo の仕組みと重要性の理解
* プログラムやサービスの実⾏⽅法の理解
* 環境変数の理解
* パッケージマネージャの使い⽅
* 実習︓ウェブサーバを⽴てる、サーバのエラーログを見てスクリプトを修正する

これぐらいできればあとは何とかなります。

## 学習環境

VirtualBox-6.1.22-144080-Win.exe  
ubuntu-20.04.2-live-server-amd64.iso  
ubuser/Password01  
VirtualBox上で起動して、任意のSSHクライアントから接続します。  
特に指定のない人はWindowsならPowerShellから。  

> $ip address show

またはここ。要Github, Twitter, Google etc login
https://www.katacoda.com/courses/ubuntu/playground

で現在のマシンのIPを表示(最近のディストリ ifconfig がない)

ssh ubuser@192.168.27.230

## 以下講師⽤メモ

!WARNING! これは教材ではありません。講師が教えるためのメモです。

### Linuxのディレクトリ構造

* Linuxのディレクトリ構造には標準ルールがあります。  
    * https://ja.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
    * 逆にいうとこれ以外はぜんぶベンダ拡張ってこと︕
* 最重要
    * /etc 設定ファイル
    * /home ユーザのホーム(~/ がエイリアス)
    * /var ログなど変化し続けるファイルの一時ディレクトリ
    * /usr/bin ユーザ⽤のプログラムおきば

* ubuntu のルートフォルダ構成
    * boot OS起動時に必要なファイル
    * etc 各種設定ファイル
    * lib /bin, /sbin にあるコマンドの実行に必要なライブラリの置き場所。lib64は64bit用
    * lost+found システムのバックアップや復元用ファイル
    * mnt 一時的なマウントポイント
    * proc プロセスIDのディレクトリ。プロセス独自の情報を格納。
    * run 実行中のデーモンが利用するフォルダ
    * snap 仮想環境用の作業フォルダ
    * sys デバイスドライバ、カーネル情報
    * usr アプリやコマンド、全ユーザで利用するコマンド
    * bin rootとユーザが両方使うコマンド
    * dev デバイスファイル
    * home ユーザごとのホームディレクトリ
    * media OSが自動的にマウントするmnt
    * opt アプリの拡張パッケージ（Chrome拡張など）
    * root rootのホームディレクトリ
    * sbin rootが使うコマンド
    * srv httpなどウェブアプリの置き場所
    * tmp 一時ディレクトリ
    * var ログなど変化し続けるファイルの一時ディレクトリ

* STDIN/STDOUT/STDERR の基本ストリームと、ストリームを繋ぐパイプ"|"、ストリームの向きを変えるリダイレクタ">","&" の理解
    * $find / hoge | more や $tail -f -5 tmpErrorLog | grep "critical error" > permanentErrorLog とか
の意味、意義を知る
    * |(パイプ) ︓STDOUTに出たやつを、パイプの次に指定したコマンドのSTDINとして処理する
    * find / httpd ってやったら無数に結果出てきて読めない＞＜ そんなときに
    * find / httpd | more ってやると、find / httpd の出⼒を more ⼊⼒にしてくれるので、スペースキーでページ送りできます
    * \>, & (リダイレクタ)︓ふつう標準出⼒や標準エラー出⼒に出る物の出⼒先を変える。
        * $someErrorProc &> /dev/null とかするとエラーでスクリーンを汚さずにすみます。 /dev/nullはshellのごみ箱、です

## ファイルエクスプローラーコマンド

* ls (list directory contets)︓今いるディレクトリのファイル⼀覧を表⽰ ※要するにフォルダをダブルクリック
* ls -la : ファイルの属性情報つき ※要するにフォルダの詳細表⽰
cd (change directory)︓フォルダ変更 ※要するにフォルダをダブルクリック
場所の指定⽅法 "." は今いる場所。 ".." は今いる場所のひとつ上の階層。"/" はルートディレクトリ。
"~"はホームディレクトリ
⾏きたいフォルダがあったらその名前を⼊れる
* pwd (print working directory)︓今いる場所の表⽰ ※要するにフォルダウインドウのパスのところ
* find ︓ファイル検索 ※要するにCtrl+F
* find /home/ -name "hoge*"
* touch︓ファイルの新規作成 ※要するに新規ファイル
touch hoge.txt で、いまいる場所に hoge.txt の空ファイルができます
* more: ファイルの中⾝を⾒る
lessだろ常考、ってひともいますけど、僕はシンプルなmoreが好きです
* cp: ファイルコピー cp ファイル元 ファイル先 cp -r でディレクトリごと。
* mv: ファイルの移動 書式はcpと⼀緒
リネームはmvで⾏います
* mkdir: フォルダの作成
* rm: ファイルの削除 *rm -r: フォルダの削除

### しっておこう︕
* tab キーでコマンド補完
* ⽮印キー ↑↓でコマンド履歴を辿る
* ctrl+r でコマンド履歴をプログレッシブサーチ︓超 絶 便 利 
|(パイプ) ︓STDOUTに出たやつを、パイプの次に指定したコマンドのSTDINとして処理する
    * find / httpd ってやったら無数に結果出てきて読めない＞＜ そんなときに
    * find / httpd | more ってやると、find / httpd の出⼒を more ⼊⼒にしてくれるので、スペースキーでページ送りできます
* ctrl+c でいまフロントにあるプロセスを強制停⽌
    * find / httpd | more で、読むのに飽きたら ctrl+c してみましょう
* clear コマンドで、なんかゴチャゴチャした画⾯をスッキリできます
* which コマンドで、⾃分が打っているコマンドがどこに置いてあるのか、わかります。 which ls ってやってみよう

>$which ls  
>/bin/ls

パスは /bin/ls です。知ってた。

### この辺でUNIX哲学
>・⼀つのことを⾏い、またそれをうまくやるプログラムを書け。  
>・協調して動くプログラムを書け。  
>・標準⼊出⼒（テキスト・ストリーム）を扱うプログラムを書け。  
>標準⼊出⼒は普遍的インターフェースなのだ。  
>                    — M. D. マキルロイ、UNIXの四半世紀  

仕事もそうですよねー

>・ユーザは自分が何をしようとしているか知っている

### ファイルの関連付け という概念はない

特にCLIで利⽤する場合、Windowsで利⽤できた「拡張⼦とそれを開くアプリケーション」という概念はありません。常に、それを開くアプリケーションを⾃分で指定します。唯⼀、拡張⼦に意味があるのは、テキストエディタ側で、プログラミング⾔語を⾒分けて、⾊分けしてくれる、ような場合でしょうか。

### テキストエディタの操作

* vim で。emacs派ですけど、ここはvimで。
* vim hoge.txt で hoge.txt を新規作成してOPEN
    * 何もないファイル操作しても⾯⽩くないので、 wget https://www.ietf.org/rfc/rfc2616.txt として、⻑い⽂書取ってきましょう
    * vim rfc2616.txt
        * 手で打たない！！
* 最低限の操作。vim はモードと切り替えながら操作する。
    * ノーマルモード(ファイルを開いたり、読んだり): esc
    * 挿⼊モード(ファイルの中⾝を編集)︓a
    * 行コピー（ヤンク）:ノーマルモードで yy
    * ペースト:ノーマルモードで  p
    * 行削除:ノーマルモードで  dd
    * 単語のコピー：v で範囲選択して y
    * esc-v：ビジュアルモードへ移行

!ターミナルによってはビジュアルモードの編集がうまく行かないことがあります。

* ノーマルモードのあと、qで終了、wで保存、wqで保存して終了。q! で、変更点があっても強制終了。
* とにかく、困ったらesc︕困ったらesc︕

あとはチートシートをみる
http://vim.rtorr.com/lang/ja/

### パーミッションの概念の理解


読み込み︓R(4)、書き込み︓W(2)、実⾏︓X(1)  
R W X R W X R W X  
[オーナー][グループ][それ以外]  
権限が付与されているなら()内の数値が⽴つ。  
例えば「RW-Rw--R--」は [4+2+0][4+2+0][4+0+0]で「664」  

644は 「オーナーは RW、グループはRW、それ以外はR」ということで、⼀般的なテキスト、設定ファイルに付与され
る権限755は 「オーナーは RWX、グループはRX、それ以外もRX 」ということ、⼀般的な実⾏ファイルに付与される権限。
なお、Xがないとディレクトリの参照もできない

>linux-tutorial-00@linux-tutorial-00:~$ ls -l hoge.txt
>-rw-rw-r-- 1 linux-tutorial-00 linux-tutorial-00 0 Feb 18 02:58 hoge.txt

これは、hoge.txt の属性情報で、
* ファイル情報。- は一般ファイル。dはディレクトリ lはシンボリックリンク 
* オーナーはRW、グループはRW、それ以外はR。
* ハードリンク数は１
    * 同じデバイス内にある別名。特に気にしなくてOK
* 所有者は linux-tutorial-00
* 所有グループは linux-tutorial-00
* ファイルサイズは0
* 更新日時は Feb 18 02:58
* ファイル名は hoge.txt

### 環境変数について

環境変数は、プログラムの実行時に挙動を調整するためのパラメータで、プロセスごとに設定される。現在みなさんが実行しているプロセスは、shell/bash。例えば、ls というコマンド＝プログラムが、ls だけで実行できるのは、環境変数PATHに、lsの実行ファイルが格納されているディレクトリまでのパスが書いてあるから。

### sudo の仕組みと重要性の理解

Linuxはスーパーユーザーで使ってはいけません。テストしないで出荷するようなもんです。どうしても管理者権限が必要な場合だけ、代わりに、sudoコマンド を使いましょう。azure は最初から使えますが、（さくらの）CentOSなどではそこだけsuになったあと /etc/sudoers を visudo コマンドを使って、利⽤できるユーザ等細かな設定を⾏います。

* ちなみに、コマンドプロンプトの頭が # になっているときはスーパーユーザーです。普段は $ です。

！sudo したときには環境変数が変わることを覚えておこう！

> $printenv  
> $sudo printenv

で出力が異なる。PATHが異なっていることを確認しよう。現在のユーザの環境変数を引き継いで sudo したいときは -E オプションを使う（ただ、一部引き継がれないものもあるので全面的に信頼はNG）

## プログラムやサービスの実⾏⽅法の理解

### プログラム

プログラムは ./ を付けて実⾏。シェルスクリプトやコンパイル済みのオブジェクトファイルは、ファイルの頭に ./
を付けることで明⽰的に”実⾏”されます。
※実⾏権限が必要です。

演習

>$vim hoge.sh  
>echo "hello bash"  
>esc-wq!  
>$./hoge.sh -> Permission denied.  
>$chmod 755 hoge.sh  
>$./hoge.sh  
>hello bash  

### パッケージマネージャの使い⽅

* tree コマンドがない︕ありえない︕
* $sudo apt install tree
* $tree .
* 癒されたー もう tree いいや
* $sudo apt remove tree
* $sudo apt list いま入っているパッケージの一覧
* パイプと組み合わせて tree が入っているかを確認

### サービスの話とウェブサーバを立てる実習

* service --status-all: 今動いているサービスの確認
    * +: 稼働中 -:停止中 ?:状態不明

* apt で httpd をインストールする
    * sudo apt install apache2
* サービスで apache2 が起動していることを確認する
* http://ip でアクセスしてみる

>$systemctl start apache2  
>$systemctl stop apache2  
>$systemctl restart apache2  

### index.html を書き換えよう

apache2の設定ファイルは apache2.conf。  
/etc/apache2/apache2.conf  

index.html は 
vim で index.html を書いて、表⽰させてみましょー  

>$sudo vim /var/www/html/index.html

## サーバ管理でエラーと戦ってみよう

* apache止める
	* systemctl stop apache2
* 設定ファイルいじる
	* sudo vim /etc/apache2/apache2.conf
	* 98 - G で98行目にジャンプ
	* KeepAlive On の K を消しちゃう
		* 設定ファイルを誤った、状況
* apache動かす
	* systemctl start apache2
* 動かない
	* 原因は想像つくけど、調査しよう
	* journalctl -xe
	* モロに書いてある
	* 修正しよう
	* sudo vim /etc/apache2/apache2.conf
* apache動かす
	* systemctl start apache2
* service --status-all
	* 動いてる
