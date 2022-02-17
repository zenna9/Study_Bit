
boo = True
while boo is True :
    print("수를 입력하세요")
    inp = input()

    if inp.isnumeric() is False :
        print("정수가 아닙니다. 다시 입력")
    elif inp.isnumeric() is True:
        intinp = int(inp)
        print("1부터 {}까지 3의 배수의 합 : ".format(intinp), end="")
        sum=0
        for i in range(2, intinp) :
            if i %3 == 0 :
                sum +=i
        print(sum)

