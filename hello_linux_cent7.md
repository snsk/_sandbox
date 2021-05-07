## これはなに

Linux初学者向け講座の講師⽤メモです。Linuxほぼ触ったことがない⼈向け。これを終えると以下ができるようになります。

* Linuxのディレクトリ構造の理解
* ファイルエクスプローラー操作
* テキストエディタの操作
* パーミッションの概念の理解
* sudo の仕組みと重要性の理解
* プログラムやサービスの実⾏⽅法の理解
* パッケージマネージャの使い⽅
* おさらい実習︓ウェブサーバを⽴てる、CGIを触る

これぐらいできればあとは何とかなります。

## 学習環境

amazon ec2 t2.micro

ログインは適当なsshクライアントで、
>$ chmod 600 SSH_KEY  
>$ ssh -i SSH_KEY ec2-user@INSTANCE_PUBLIC_IP

これがすでにLinuxコマンドなんですけど、、、というツッコミは⽢んじて受けます、、

## 以下講師⽤メモ

!WARNING! これは教材ではありません。講師が教えるためのメモです。

### Linuxのディレクトリ構造

* Linuxのディレクトリ構造には標準ルールがあります。  
    * https://ja.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
    * 逆にいうとこれ以外はぜんぶベンダ拡張ってこと︕
* 最重要 → /etc 設定ファイル、 /home ユーザのホーム(~/ がエイリアス)、/
var 捨てファイル、/usr/bin ユーザ⽤のプログラムおきば
* STDIN/STDOUT/STDERR の基本ストリームと、ストリームを繋ぐパイプ"|"、ストリームの向きを変えるリダ
イレクタ">","&" の理解
    * $find / hoge | more や $tail -f -5 tmpErrorLog | grep "critical error" > permanentErrorLog とか
の意味、意義を知る
    * |(パイプ) ︓STDOUTに出たやつを、パイプの次に指定したコマンドのSTDINとして処理する
    * find / httpd ってやったら無数に結果出てきて読めない＞＜ そんなときに
    * find / httpd | more ってやると、find / httpd の出⼒を more ⼊⼒にしてくれるので、スペースキーでページ送りできます
    * >, & (リダイレクタ)︓ふつう標準出⼒や標準エラー出⼒に出る物の出⼒先を変える。
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

>alias ls='ls --color=auto'
>/bin/ls

ls は ls --color=auto として実⾏されてます  
パスは /bin/ls です。知ってた。

### この辺でUNIX哲学
>・⼀つのことを⾏い、またそれをうまくやるプログラムを書け。  
>・協調して動くプログラムを書け。  
>・標準⼊出⼒（テキスト・ストリーム）を扱うプログラムを書け。  
>標準⼊出⼒は普遍的インターフェースなのだ。  
>                    — M. D. マキルロイ、UNIXの四半世紀  

仕事もそうですよねー

### ファイルの関連付け という概念はない

特にCLIで利⽤する場合、Windowsで利⽤できた「拡張⼦とそれを開くアプリケーション」という概念はありません。
常に、それを開くアプリケーションを⾃分で指定します。唯⼀、拡張⼦に意味があるのは、テキストエディタ側で、
プログラミング⾔語を⾒分けて、⾊分けしてくれる、ような場合でしょうか。
  
Windowsのコマンドプロンプトでは、open hoge.txt でメモ帳が起動してくれますが、Linuxの open は (2)、システムコールです。file descriptorを return します。
  
$man open としてマニュアルを読んでみましょう。

### テキストエディタの操作

* vim で。emacs派ですけど、ここはvimで。
* vim hoge.txt で hoge.txt を新規作成してOPEN
    * 何もないファイル操作しても⾯⽩くないので、 wget https://www.ietf.org/rfc/rfc2616.txt として、⻑い⽂書取ってきましょう
* 最低限の操作。vim はモードと切り替えながら操作する。
    * ノーマルモード(ファイルを開いたり、読んだり): esc
    * 挿⼊モード(ファイルの中⾝を編集)︓a
    * ビジュアルモード(⾏単位でのコピペなど)︓v
* ノーマルモードのあと、qで終了、wで保存、wqで保存して終了。q! で、変更点があっても強制終了。
* とにかく、困ったらesc︕困ったらesc︕

あとはチートシートをみる
http://vim.rtorr.com/lang/ja/

### パーミッションの概念の理解


読み込み︓R(4)、書き込み︓W(2)、実⾏︓X(1)  
R W X R W X R W X  
[オーナー][グループ][それ以外]  
権限が付与されているなら()内の数値が⽴つ。  
例えば「RW-R--R--」は [4+2+0][4+0+0][4+0+0]で「644」  

644は 「オーナーは RW、グループはR、それ以外もR」ということで、⼀般的なテキスト、設定ファイルに付与され
る権限755は 「オーナーは RWX、グループはRX、それ以外もRX 」ということ、⼀般的な実⾏ファイルに付与される権限
さっきSSHに設定した 600 は「持ち主以外⼀切触れない」権限。なお、Xがないとディレクトリの参照もできない

>[ec2-user@ip-172-31-1-227 ~]$ ls -la hoge.txt
>-rw-rw-r-- 1 ec2-user ec2-user 0 Apr 22 03:15 hoge.txt

これは、hoge.txt の属性情報で、
オーナーはRW、グループはRW、それ以外はR。サイズは1バイトで、所有者はec2-user、属するグループはec2-
user、更新⽇は 0年4⽉22⽇3:15、ファイル名は hoge.txt
と⾔っている。更新⽇がおかしいのはLANG設定のせい。


### sudo の仕組みと重要性の理解

Linuxはスーパーユーザーで使ってはいけません。テストしないで出荷するようなもんです。  どうしても管理者権限が必要な場合だけ、代わりに、sudo+コマンド を使いましょう。ec2 は最初から使えますが、（さくらの）CentOSなどではそこだけsuになったあと /etc/sudoers を visudo コマンドを使って、利⽤できるユーザ等細かな設定を⾏います。

* ちなみに、コマンドプロンプトの頭が # になっているときはスーパーユーザーです。普段は $ です。

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

### サービス

* chkconfig: OS起動時にONになるサービスの確認  
* service --status-all: 今動いているサービスの確認
いまログインしてるランレベルは3

>Run Level  
>0 システムの停⽌  
>1 シングルユーザモード  
>2 マルチユーザモード  
>3 マルチユーザモード(コンソールログイン)  
>4 未使⽤  
>5 マルチユーザモード(ディスプレイマネージャ使⽤)  
>6 システム再起動  

* sendmail してみよっか

>[ec2-user@ip-172-31-1-227 ~]$ sendmail shinsk@gmail.com  
>From: shinsk@gmail.com  
>To: shinsk@gmail.com  
>Subject: hoge  

* sendmail ⽌めてみよっか

>$ sudo /etc/init.d/sendmail stop -> とばない
>$ sudo /etc/init.d/sendmail start -> とぶ

sendmail はメールをキューイングするので、start した瞬間にとぶ。

* メールの⼩話︓
    * smtp の仕様上、必須フィールドは実はto のみ。あとはエンベロープとよばれる領域。MAIL FROM,RCPT TO, BODYで、 あとは実はbody部。from無しを受け付けるかどうかは次のMTAの仕様
    * サービスの利⽤確認で sendmail はやめたほうがいいね、、、何か考えます

### パッケージマネージャの使い⽅

* tree コマンドがない︕ありえない︕
* $sudo yum install tree
* $tree .
* 癒されたー もう tree いいや
* $sudo yum remove tree

### おさらい実習︓ウェブサーバを⽴てる、CGIをさわる

いまどきApacheもない気がしますけど簡単だから

>$ sudo yum install httpd  
>$ sudo /etc/init.d/httpd start  

### index.html を書き換えよう

index.html はどこにおく︖ 設定ファイルに書いてあります。document_rootです
apacheの設定ファイルは httpd.conf。
vim で index.html を書いて、表⽰させてみましょー。  

http://publicip/ です。  

python スクリプトをうごかしてみよう

$ sudo vim /etc/httpd/conf/httpd.conf

>AddHandler cgi-script .cgi .py ★これ追加  
>ScriptAlias /cgi-bin/ "/var/www/html/" ★document_rootに書き換え  
><Directory "/var/www/html"> ★document_rootに書き換え  
> AllowOverride None  
> Options ExecCGI ★これ追加  
> Order allow,deny  
> Allow from all  
></Directory>  

$ sudo vim /var/www/html/hoge.py

~~~python
#!/usr/bin/python
# coding:utf-8
import cgi
form = cgi.FieldStorage();
name = "";
if ( form.has_key("name") ):
 name = form["name"].value
print "Content-Type: text/html\n";
print "Hello World!";
print "Hi! " + name ;
~~~

【重要】コピペOKですが、原則として、⾃分が書いた(貼った) コードは全⾏⾃分で解説できるべきです。
↓

* アクセスするとテキストでくる
* $sudo /etc/init.d/httpd restart
* ぱーみっしょんえらー
* $sudo chmod 755 /var/www/html/hoge.py
* でました︖ たぶんこんごCGI使うことないです。はい。


## CGIのかんたんな解説

* CGIとPerl、CGIとPythonはDOMとJavaScriptの関係にそっくりです
* CGIはブラウザがサーバに送信する環境変数やHTTP リクエストのBODY部の情報を、サーバ側がどのように受け取るか、そのインターフェースを定義した”仕様”です
    * CGI⾃体がプログラムなわけではありません、インターフェース仕様です。DOMと⼀緒。
* HTTPリクエスト、GETの引数についてくるのは環境変数の QUERY_STRING。POSTのBODY部は STDIN に⼊ってきます。
    * cgi.FieldStorage(); でHTMLのform要素の各値をPythonで扱いやすい構造（連想配列)に変換してくれてます
    * 上のコードでは連想配列に変換したあとに、その配列⾃体が name というキーを持っているか確認して、持っていたら表⽰のための⽂字列型変数に格納する、という処理をしています
* この⽅法でブラウザとサーバでデータをやりとりする、というのは太古のアーキテクチャなので、今後新規のウェブ開発で意識的に使うことはまずありません
    * 現代はDBありきのアーキテクチャが主流です。インフラを除くウェブ技術としては、CRUDをURLで操作するREST、ルーティング、MVCあたりを抑えたうえで、クライアントサイドでのコンポーネント技術であるreactあたりをフムフムと読んでおくとよいでしょう
