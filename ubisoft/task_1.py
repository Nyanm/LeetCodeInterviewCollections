def linear_merge(list1, list2):
    len1, len2 = len(list1), len(list2)
    neo, index1, index2 = [], 0, 0

    while True:
        if index1 == len1 and index2 == len2:
            break
        if index1 == len1:
            for index in range(index2, len2):
                neo.append(list2[index])
            break
        if index2 == len2:

            for index in range(index1, len1):
                neo.append(list1[index])
            break
        if list1[index1] < list2[index2]:
            neo.append(list1[index1])
            index1 += 1
        else:
            neo.append(list2[index2])
            index2 += 1
    return neo


if __name__ == '__main__':
    print(linear_merge(['aa', 'xx', 'zz'], ['bb','cc']))
