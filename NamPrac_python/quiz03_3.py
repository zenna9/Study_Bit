def whatyouwant(*a):
    total = 0
    for i in a :
        total += i
    print("total : ",total)
    print("최대값 : ",max(a))
    print("최소값 : ",min(a))
    print("평균 : ", total/len(a))

whatyouwant(1, 2, 3, 4)