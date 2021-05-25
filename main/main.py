import PySimpleGUI as sg
import random

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