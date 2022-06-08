def compress(chars):
    if len(chars) <= 1:
        return len(chars)
    cnt, color = 0, chars[0]
    res = []
    for char in chars:
        if char == color:
            cnt += 1
        else:
            res.append(color)
            if cnt > 1:
                res.append(str(cnt))

            color = char
            cnt = 1
    res.append(color)
    if cnt > 1:
        res.append(str(cnt))

    res = ''.join(res)
    for index in range(len(res)):
        chars[index] = res[index]

    return len(res)



if __name__ == '__main__':
    print(compress(['a']))
