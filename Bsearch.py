pos = -1


def search(nums, n):
    f = 0
    u = len(nums) - 1

    while f <= u:
        mid = (f + u) // 2

        if nums[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if nums[mid] < n:
                f = mid + 1
            else:
                u = mid - 1


nums = [2, 3, 4, 5, 6, 11, 13, 44, 55, 77, 88, 99]
n = int(input("enter the number you want to search"))

if search(nums, n):

    print("value is found at", pos + 1)

else:
    print("value is not found")
