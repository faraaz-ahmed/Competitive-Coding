def generate_8(n):
    x = ""
    for i in range(0, n):
        x += "8"
    return int(x)
def nearest_even_number(num):
    x = int(num)
    arr = []
    while x>0:
        arr.append(x%10)
        x = x/10
    index = 0
    arr.reverse()
    # print("first", arr)
    for i in range(0, len(arr)):
        if arr[i] % 2 == 1:
            break
        else:
            index = index + 1
    # print("my real index", index)
    scale_up = 0
    if index == len(arr):
        return 0
    else:
        # print("my_index", index, arr)
        temp_index = index + 1
        if index == len(arr) - 1:
            return "1"
        else:
            # if arr[index + 1] == 5:
            #     while index < len(arr):
            #         temp_index = temp_index + 1
            #         if arr[temp_index] == 5:
            #             continue
            #         elif arr[temp_index] > 5:
            #             scale_up = 1
            #             break
            #         elif arr[temp_index] < 5:
            #             break
            #     if scale_up == 1 or temp_index == len(arr):
            #         arr[index] = arr[index] + 1
            #         for i in range(0, index):
            #             arr[i] = 0
            #     elif scale_up == 0:
            #         arr[index] = arr[index] - 1
            #         for i in range(0, index):
            #             arr[i] = 8
            # elif arr[index - 1] < 5:
            #     arr[index] = arr[index] - 1
            #     for i in range(0, index):
            #         arr[i] = 8
            # elif arr[index - 1] > 5:
            #     arr[index] = arr[index] + 1
            #     for i in range(0, index):
            #         arr[i] = 0
            extract = []
            for i in range(index + 1, len(arr)):
                extract.append(arr[i])
            number = int(''.join(map(str,extract)))
            upper_limit = 10**len(extract) - number
            lower_limit = number + (upper_limit - generate_8(len(extract)))
            # print("extract = ", extract,"upper_limit =", upper_limit, "lower_limit =", lower_limit)
            if upper_limit > lower_limit:
                arr[index] = arr[index] - 1
                for i in range(index + 1, len(arr)):
                    arr[i] = 8
            else:
                arr[index] = arr[index] + 1
                for i in range(index + 1, len(arr)):
                    arr[i] = 0
        # print(int(''.join(arr)),"arr")
        # print("array before reversing", arr)
        # arr.reverse()
        # print(arr)
        final = []
        for i in range(0, len(arr)):
            final.append(str(arr[i]))
        # print(''.join(arr))
        # print(int(num),"actual number")
        return str(abs(int(''.join(map(str,arr))) - int(num)))
t = int(input())
for i in range(0, t):
    n = input()
    st = "Case #" + str(i + 1) + ": " + str(nearest_even_number(n))
    print(st)
