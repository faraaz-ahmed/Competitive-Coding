def round(num):
    if num % 2 == 1:
        return int((num + 1)/2)
    else:
        return int(num/2)

def brute_minSum(arr, k):
    sum_ = sum(arr)
    for i in range(0, k):
        sum_ -= round(max(arr))
        arr[arr.index(max(arr))] = round(arr[arr.index(max(arr))])
    print(arr)
    return sum(arr)

# def minSum(arr, k):
#     x = list(arr).sort(reverse = True)
#     my_dict = {}
#     for i in range(0, len(arr)):
#         my_dict[i] = arr[i]
#     max_1 = x[0]
#     max_2 = x[1]
#     for i in range(0, len(arr)):

# test cases
print(brute_minSum([10, 20, 7], 4))

print(brute_minSum([2],1))

print(brute_minSum([2, 3], 1))
