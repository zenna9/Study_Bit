
def badman_goodman(score1, score2):
    if score1>=50 and score2 >=50 :
        if (score1+score2)/2 >=60 :
            print("합격")
    else :
        print("불합격")

badman_goodman(49, 71)
