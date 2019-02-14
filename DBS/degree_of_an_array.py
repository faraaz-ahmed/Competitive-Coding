def degree(arr):
    hash = {}
    keys = list(set(arr))
    keys.sort()
    # print(keys)
    for i in range(0, len(keys)):
        hash[keys[i]] = 0
    for i in range(0, len(arr)):
        hash[arr[i]] = hash[arr[i]] + 1
    final_sort = []
    # for i in range(0, len(keys)):
    #     for j in range(0, hash[keys[i]]):
    #         final_sort.append(keys[i])
    # print(x)
    x = hash.items()
    x1 = sorted(x, key = lambda x : x[1], reverse = True)
    y = x1[0][1]
    x = list(filter(lambda x : x[1] == y,x))
    # print(x)
    final = []
    for i in range(0, len(x)):
        count = 0
        index = 0
        for j in range(0, len(arr)):
            if count == 0 and arr[j] == x[i][0]:
                count += 1
                index = j
            elif count > 0 and arr[j] == x[i][0]:
                count += j - index
                index = j
        final.append([x[i][0], count])
    # print(final)
    x1 = sorted(final,key = lambda x : x[1] )
    # print(x1)
    y = x1[0][1]
    return list(filter(lambda x : x[1] == y,final))[0][1]
    # print()



print(degree([1,2,1,3,2]))
print(degree([1,2,2,3,1]))
print(degree([1,1,2,1,2,2]))
