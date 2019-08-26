#141

import hello_func
import greeting_func

def main():
    print("insa_func 모듈입니다.")
    print("__name__: ",__name__)    #실행하면 __main__이 출력됨
    hello_func.hello()
    greeting_func.greeting()

main()