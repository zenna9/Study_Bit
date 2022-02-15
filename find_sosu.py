def sosu_list(find_until):
    result = [2, 3, 5]
    i = 6

    while i < find_until:
        # i는 6에서 find_until까지 증가하며 소수인지 확인될 것
        for a_from_list in result:
            # a_from_list는 result 안의 숫자들. i와 비교할 것
            if i % a_from_list == 0:
                # i를 a_from_list로 나눠 소수가 아니면 result에서 뺄것(true)
                boo = True
                break
            elif i % a_from_list != 0:
                boo = False

        if boo is False:
            result.append(i)
        i += 1
    return result

sosu = sosu_list(1000+999+998)
nums = [1,2,7,6,4]

def solution(nums):
    nums.sort()
    nums_len = len(nums)

    count_can_sosu = 0
    for a in range(0, nums_len) :
        for b in range(a+1, nums_len) :
            for c in range(b+1, nums_len):
                summ = nums[a]+nums[b]+nums[c]
                if sosu.count(summ) == 1 :
                    # summ 이 소수 리스트인 nums에 몇개 있는지 반환. 0이면 소수가 아님
                    count_can_sosu += 1
    return count_can_sosu

print(solution(nums))
