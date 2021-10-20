# test4
<h1 align = "center">
  <br>
  <a href="img" ><img src = "https://user-images.githubusercontent.com/69783019/119460348-8aa9ac00-bd79-11eb-8afc-cbcc0d26c1f0.png" width="500" alt = " ArminC AutoExec ">
  </a>
</h1>
<p align="center">
  <h2 align="center">じゃんけんGUIアプリ化</h2>
</p>
<p align="center">
  <a href="https://img.shields.io/badge/Python-v3.9.0-blue">
    <img src="https://img.shields.io/badge/Python-v3.9.0-blue"alt="python">
  </a>
  <a href="https://img.shields.io/badge/PySimpleGUI-4.39.1-blue">
    <img src="https://img.shields.io/badge/PySimpleGUI-4.39.1-blue"alt="PySimpleGUI">
  </a>

![demo](https://user-images.githubusercontent.com/69783019/119269282-d2252080-bc31-11eb-8815-c104de787a8b.gif)


# 概要
簡単なじゃんけんプログラムをPySimpleGUIを使いGUIアプリ化

# PyPI
Python GUIのモジュールとしてPySimpleGUIを使います

```pip
$ pip install PySimpleGUI
```

# 構造

## モジュール

PySimpleGUI
* GUIの作成

random
* 毎回ランダムな数値を出す

```python
import PySimpleGUI as sg
import random
```

## じゃんけんプログラム

`rsp()`関数はランダムに決められた数値とボタンを押されたときの数値を入れて処理している

画面に`sg.popup_quick_message`を使いメッセージを出す

```python
def rsp(computer, player):
    if computer == 1:
        comp = "グー"
    elif computer == 2:
        comp = "チョキ"
    else:
        comp = "パー"

    if computer == 1 and player == 3 or computer == 2 and player == 1 or computer == 3 and player == 2:
        sg.popup_quick_message(f"コンピュータの手{comp}\nあなたの勝ちです", font=(20), text_color='#ffff00')
    elif computer == 3 and player == 1 or computer == 1 and player == 2 or computer == 2 and player == 3:
        sg.popup_quick_message(f"コンピュータの手{comp}\nあなたの負けです", font=(20), text_color='#ff4500')
    else:
        sg.popup_quick_message(f"コンピュータの手{comp}\nあいこです", font=(20))
```

## 画面

`layout`
* 二次元配列でウィンドウレイアウトを決める
* `sg.B` ボタンの表示
* `image_filename` ファイルから相対パスで画像ファイルを取得している
* `k` ボタンそれぞれの辞書型のキーの設定

`event`
* このプログラムではボタンが押されたときのイベント


```python
layout = [
        [sg.B(image_filename="img/choki.png", k="choli"), sg.B(image_filename="img/rook.png", k="gu"), sg.B(image_filename="img/pa.png", k="pa")]
        ]

window = sg.Window("じゃんけん", layout)

while True:
    event, value = window.read()
    cp = random.randint(1, 3)
    # print(event, value)

    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "gu": # 1
        rsp(cp, 1)
    if event == "choli": # 2
        rsp(cp, 2)
    if event == "pa": # 3
        rsp(cp, 3)

window.close()
```
  
[rps画像 いらすとや](https://www.irasutoya.com/2013/07/blog-post_5608.html)


[PySimpleGUI GitHub](https://github.com/PySimpleGUI)

[PySimpleGUIドキュメント](https://pysimplegui.readthedocs.io/en/latest/)
