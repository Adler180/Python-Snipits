def eea(a, b, arr = [], mod = []):
    #Returns the multiplicativ invers of the number b in the Field Z_a
    mod.append(a)
    if b == 0:
        #Second stage of the eea
        for i in range(0, len(arr)):
            if i == 0:
                arr[len(arr)-1-i].append(0)
                arr[len(arr)-1-i].append(1)
            else:
                arr[len(arr)-1-i].append(arr[len(arr)-i][5])
                arr[len(arr)-1-i].append(arr[len(arr)-i][4] - (arr[len(arr)-i-1][2] * arr[len(arr)-i][5]))
        return (arr[0][5]) % mod[0]
    arr.append([a, b, a//b, a%b])
    return eea(b, a%b, arr)





def create_eea_table(a, b, arr = []):
    #Returns the table structure of the eea in the following form:
    # [a, b, q, r, x, y]
    if b == 0:
        #Second stage of the eea
        for i in range(0, len(arr)):
            if i == 0:
                arr[len(arr)-1-i].append(0)
                arr[len(arr)-1-i].append(1)
            else:
                arr[len(arr)-1-i].append(arr[len(arr)-i][5])
                arr[len(arr)-1-i].append(arr[len(arr)-i][4] - (arr[len(arr)-i-1][2] * arr[len(arr)-i][5]))
        return arr
    arr.append([a, b, a//b, a%b])
    return create_eea_table(b, a%b, arr)
