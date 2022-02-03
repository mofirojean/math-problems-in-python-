"""calculating median, mode, mean"""


"""calculating the mean"""
def mean(list_num):
    total = 0
    for num in list_num:
        total += num
    return total/len(list_num)


def mode(list_num):
    max_count = (0, 0)
    for num in list_num:
        occurences = list_num.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    return max_count[1]


def median(list_num):
    list_num.sort()
    if len(list_num) % 2 != 0:
        middle_index = int((len(list_num)-1)/2)
        return list_num[middle_index]
    elif len(list_num) % 2 == 0:
        middle_index_1 = int(len(list_num)/2)
        middle_index_2 = int(len(list_num)/2) - 1
        return mean([list_num[middle_index_1], list_num[middle_index_2]])

print(median([13,13,13,13,14,14,16,16]))
