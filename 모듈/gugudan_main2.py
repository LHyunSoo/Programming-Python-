#143p gugudan_main2.py

import gugudan2

def main():
    for i in range(9,10):
        print("="*20)
        gugudan2.gugudan(i)

if __name__ == "__main__":  #자기 모듈 실행하면 실행되고, 다른 곳에서 import하면 실행 안됨
    main()