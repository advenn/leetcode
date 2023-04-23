# An in-place Python program
# to reverse an array
""" Function to reverse arr[]	from start to end"""


def reverseArray(arr, n):
    for i in range(0, int(n / 2)):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    print(*arr)
    reverseArray(arr, n)
    print("Reversed array is")
    print(*arr)

# This code is contributed
# by Harshit Saini
