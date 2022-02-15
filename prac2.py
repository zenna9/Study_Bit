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


nums = sosu_list(30)

print(type(nums.count(7)))