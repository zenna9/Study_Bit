def solution(answers):
    supo1 = [1,2,3,4,5]*int(10000/5)
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]*int(10000/8)
    supo3 =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*int(1000)
    who = [0, 0, 0]

    for i in range (0, len(answers)):
        if supo1[i] == answers[i] :
            who[0] += 1
        if supo2[i] == answers[i] :
            who[1] += 1
        if supo3[i] == answers[i] :
            who[2] += 1

    for k in range(len(who)) :
        if who[k] == max(who) :
            answer.append(k+1)
        print('k is {}, answer is {}'.format(k,answer))
    return answer
solution([1, 2, 3, 4, 5])