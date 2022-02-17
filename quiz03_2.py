
lst = [1, 3.14, 'python', 7, 89.1, 3]
lst_cleaned = list()

for i in range(0, len(lst)) :
    if (type(lst[i]) is int) or (type(lst[i]) is float) is True :
        lst_cleaned.append(lst[i])
print(lst_cleaned)