'''
動くPython3文法確認
複数行コメントは クォート3つ で囲む
インライン（行内) コメントは ＃

※注意※
このスクリプトを実行すると、同じフォルダに "python3_grammar_temp.txt"
というテキストファイルが生成されます。これは以下のプログラムでファイル書き込みの例文があるためです。

'''

''' 
計算
'''
print("<加減乗除商>")
print(1 + 1)
print(2 - 1)
print(2 * 2)
print(10 / 3)
print(10 % 3)

''' =======================================
変数宣言と制御構文
======================================= ''' 
print("<条件分岐 if文>")
x = 1 #ここを書き換えると以下のif文の動作が変わる
if x == 1:
    print("x equal 1.")
else:
    print("x not equal 1.")

print("<ループ for文>")
for i in range(5): #range オブジェクトを使ってイテレート
    print("print this " + str(i) + " times.") #変数iは数字なのでそのままでは文字列と足し算ができない。文字列に変換してから連結

print("<ループ while文>")
i = 0
while True: #while の次に書かれる条件文が True の限りループし続ける
    print("print this " + str(i) + " times.")
    i += 1
    if i > 4:
        break #ほっとくと無限ループになるので i が4を超えたら break（ループ抜ける）する

''' =======================================
関数宣言と利用、例外の捕捉
======================================= ''' 

print("<関数定義>")
def user_func1(arg1, arg2): #ここで関数を定義して
    return arg1 + arg2
print(user_func1(1, 1))  #ここで関数を使っている

#yield を使った generator の生成とその iteration。 
#yield を含む関数は戻り値として generator を返す。
#返ってきた generator は 組込関数 next() で yield を順番に実行していく

def user_func2():
    yield "one"
    yield "two"
    yield "three"
x = user_func2()
print(next(x))
print(next(x))
print(next(x)) #yield は3つしかないので、次で StopIteration 例外がでる。プログラムの実行を続けるために例外を捕まえておく。
try:
    print(next(x))
except StopIteration:
    print("there is no yield expression.")

''' =======================================
ファイル書き込み
======================================= ''' 
print("<ファイル書き込み>")
f = open("./python3_grammar_temp.txt", mode='w') #書き込みモードでファイルオープン
f.write("hello python!") #ファイル書き込み
f.close #ファイルを閉じる
f = open("./python3_grammar_temp.txt") #modeを省略すると読み込みモード 
print(f.read()) #ファイル全体を文字列として読みこんで print
f.close

''' =======================================
クラス
======================================= ''' 
print("<クラス>")
class Company: #クラス名の先頭は大文字
    name = "No name." #クラス変数
    area = "Not defined."
    employee_head_count = 0
    __secretNumber = 42 #private 変数

    #python のクラスメソッド定義の第1引数は必ず self
    def __init__(self, name, area, employee_head_count): #コンストラクタ
        self.name = name
        self.area = area
        self.employee_head_count = employee_head_count
    def introduction(self): #クラスメソッド
        print("We are " + self.name + "!.")

veriserve = Company("mycorp", "tokyo", 1000)
veriserve.introduction()

try:
    print(veriserve.__secretNumber)
except AttributeError:
    print("Unable to access private member from instance.")

class Co_company(Company): #クラスの継承
    pass #このクラスでは何も定義していないが、

votc = Co_company("myco-corp", "okinawa", 150)
votc.introduction() #継承元のメソッドが使える

''' =======================================
リスト、イテレータ、内包表記、無名関数
======================================= ''' 
print("<リスト、イテレータ、内包表記、無名関数>")
list1 = [1, 2, 3] #list には基本的に ”何でも” はいる
print(list1) #内容を整形して表示 ※printが偉い
print(list1[0]) #list の一番目の要素を表示

for item in list1: #リストの中身を順番に表示する
    print(item)

#リスト内包表記。リストの内容を冒頭の計算式にそって処理して、リストを返す　すごくpythonぽい
list2 = [item * item for item in list1]
print(list2)

#無名関数
x = lambda x : x + 2 #無名関数を作って任意の変数に突っ込む
print(x(5)) #関数定義なしで、2を足すという操作ができていることに注目

''' =======================================
クロージャ
======================================= ''' 
print("<クロージャ>")
def outer_func():
    count = 0
    def inc():
        nonlocal count # ひとつ外側の指定変数への代入を可能にする宣言
        count += 1
        return count
    return inc # インデントが outer_func であることに注目。 count を戻す inc() という関数の ”定義” を return している

# python に限らずクロージャは関数が定義された時の変数が静的に束縛される（例の場合は count ）ので、
# inc() を呼び出すたびに count が参照されてインクリメントされた結果、数がカウントupしていく
# 大域変数を使わずに状態を保持できる（ステートを持てる）ところが嬉しい

count = outer_func()
print(count())
print(count())
print(count())
print(count())

''' =======================================
インポートとライブラリの利用

※python では、import はどこにでも書ける
※注意※
import している numpy と matplotlib は python3 デフォルトではついてきません
Anaconda 経由でインストールした場合はついてきます。もし個別に
必要な場合は pip でインストールします
======================================= ''' 

import numpy as np
from matplotlib import pyplot

x = np.arange(-10, 10, 0.1)
y = 1 / (1 + np.exp(-x) )

pyplot.plot(x, y)
pyplot.title('figure is closed, execute the unit test.')
pyplot.grid()
pyplot.show()

''' =======================================
http でリソースを取得し、json に変換して処理して表示する

※ユーザ登録なしで利用できるAPIサービスを前提にしています。
ブラウザでこのURLにアクセスして利用できない場合はこちらもエラーになります。
======================================= ''' 

import urllib
import urllib.request, urllib.parse
import json

try:
    req = urllib.request.Request("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010") #requestを準備
    res = urllib.request.urlopen(req) #httpで天気予報のjsonデータを取得
    weather_info = json.loads(res.read()) #json に変換
except:
    print("Some network connnection error occured")
else:
    print(weather_info["forecasts"][0]["dateLabel"] + ": " + weather_info["forecasts"][0]["telop"]) #jsonをパーズして今日明日の天気を取り出して表示
    print(weather_info["forecasts"][1]["dateLabel"] + ": " + weather_info["forecasts"][1]["telop"])

''' =======================================
ユニットテスト
pythonにデフォルトでついているユニットテストモジュールで、
先ほど作ったクラスの機能テストの一部を実施
======================================= ''' 
import unittest

class ClassTestingMethods(unittest.TestCase):

    def test_votc_class(self):
        self.assertEqual(votc.area, 'okinawa')
        self.assertEqual(votc.employee_head_count, 150)

    def test_isupper(self):
        self.assertTrue(issubclass(Co_company, Company))

if __name__ == '__main__':
    unittest.main()
