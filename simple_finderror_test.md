## 問題：

* https://www.katacoda.com/courses/ubuntu/playground にアクセスしてください
  * github account でログインしてください
* Ubuntsu Playground が開きます
* 以下のcommandを入力してください（コピー＆ペーストできます）
  * apt install apache2
  * apt install nginx
* nginxのサービス起動でエラーが出ます
* nginxのエラーログを調査して、起動しない理由が書いてある箇所を示してください
  * ログの内容をコピー＆ペーストでOKです
* 分かれば、何が起きているかも教えてください

## 回答と解説

* 回答例：2022/04/26 06:57:55 [emerg] 2953#2953: listen() to [::]:80, backlog 511 failed (98: Address already in use)
  * 日付やPID等は各自の環境で異なる
  * $ tail /var/log/nginx/error.log に書いてある

* 解説：先にインストールして起動している apache2 がポート80を塞いでいるだけ
* apache2も、nginxも、同じ httpd（ウェブサーバー）なので、どちらも起動時にポート80を取りに行く。 apache2を先にインストールしているので、あとに入れた nginx がポート80を取れないよー、とエラーを吐いている
