a=True
sum = 0
print("q:빠져나감/ d:입금 / w: 인출")
urinput = input()

while a is True :
    if urinput == "q":
        print("종료")
        a is False
        break
    elif urinput == "d" :
        print("금액입력")
        pluss = int(input())
        sum += pluss
        print("잔액은 {}원 입니다".format(sum))
        a is True
        pass
    elif urinput == "w":
        print("금액입력")
        minuss = int(input())
        sum -= minuss
        print("잔액은 {}원 입니다".format(sum))
        a is True
    else :
        print("??")
        a is True