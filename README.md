# handwritten_numeral_recognition_by_mnist__hack

Warning : This application server is stopping now.
I will run it on another server.



On your PC, write number by your pointer. Then, NN recognize what number you wrote.

<a href="http://ec2-52-199-237-194.ap-northeast-1.compute.amazonaws.com/cgi-bin/handwritten_numeral_recognition_application_by_mnist/py.py">My application</a>


# 使い方

- まずサイト内の黒枠に１桁の数字を書く。（右クリックしながらドラック）
- 次に黒枠の下にある "Finish Drawing" のボタンを押す。（すると黒枠の右側にコピーが作成される）
- 最後に "send to ROBOT" のボタンを押すと、結果を返してくれる。

# 注意

MNISTのテストデータである程度の精度は出ていますが、PC上で書いた数字に対する認識精度はあまり高くありません。（入力データを白黒で認識させてしまっているからだと思われます。ただいま修正を試みています。）


