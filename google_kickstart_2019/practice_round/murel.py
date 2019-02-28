def round(num):
    if num - int(num) > 0.5:
        return int(num)
    else:
        return int(num) + 1
        

t =  input()
for i in range(0, int(t)):
    n = int(input())
    str = input()
    arr = list(str)
    half_sum = 0
    for i in range(0, round(len(arr)/2)):
        half_sum += arr[i]
    max_sum = half_sum
    first, last = 1, round(len(arr)/2)
    while True:
        if last == len(arr):
            break
        half_sum = half_sum - arr[first] + arr[last]
        first += 1
        last  += 1
        if max_sum < half_sum :
            max_sum = half_sum
    
    output = "Case #" + t + ":" + " " + max_sum
    print(output)
        
    
