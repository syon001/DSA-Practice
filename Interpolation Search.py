def interpolationsearch(arr, lo, hi, x):
    if lo <= hi and arr[lo] <= x <= arr[hi]:

        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolationsearch(arr, pos + 1,
                                       hi, x)

        if arr[pos] > x:
            return interpolationsearch(arr, lo,
                                       pos - 1, x)
    return -1


arr = [12, 32, 43, 54, 67, 90, 101]
n = len(arr)

x = int(input("enter the element"))
index = interpolationsearch(arr, 0, n - 1, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
