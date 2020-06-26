# import django
#
# print(django.__version__)
#
# a = 3
# b = "123"
#
# print(a * b)

# def countSignals(frequencies, filterRanges):
#
#     Freq = frequencies
#     finalNums = []
#     spareNums = []
#     trashNums = []
#     print("\nGood: ", finalNums)
#     print("Spare: ", spareNums)
#     print("Trash: ", trashNums)
#
#
#     def filterOne():
#         for FR1 in filterRanges:
#             # print(FR1)
#             for FQ in Freq:
#                 # print(FQ)
#                 if FR1[0] <= FQ <= FR1[1]:
#                     spareNums.append(FQ)
#                     # Freq.remove(FQ)
#                 else:
#                     trashNums.append(FQ)
#                     # Freq.remove(FQ)
#
#     filterOne()
#     print("\nGood: ", finalNums)
#     print("Spare: ", spareNums)
#     print("Trash: ", trashNums)
#
#
#
#     def filterTwo():
#         newA = list(set(spareNums))
#         newB = list(set(trashNums))
#         # print("\n", newA, newB)
#
#         for A in newA:
#             # print(A)
#             for B in newB:
#                 # print(B)
#                 if A == B:
#                     newA.remove(A)
#                 else:
#                     finalNums.append(A)
#
#         print("\n****HERE*****", newA)
#
#
#
#     filterTwo()
#     print("\nGood: ", finalNums)
#     print("Spare: ", spareNums)
#     print("Trash: ", trashNums)
#
#
#
# countSignals([7, 1, 15, 56, 13, 14], [[11,17], [13, 14], [14, 17] ])





# n = int(input())
# a = list(map(int, input().split()))
# a = sorted(a)
#
# ans = n - 1
#
# for i in range(n):
#     j = i
#     while j < n and a[i] == a[j]:
#         j += 1
#     ans = min(ans, n - (j - i))
#
# print(ans)


# arr = ["a", "b", "a", "c", "a"]
#
# result = dict((i, arr.count(i)) for i in arr)
#
# print(result)

# def equalizeArray(arr):
#
#     # la = len(arr)
#     x = 0
#     extraArr = []
#
#     for i in arr:
#         AC = arr.count(i)
#         # print(AC)
#         if AC >= x:
#             x = AC
#             # print(x)
#         elif AC < x:
#             extraArr.append(i)
#
#     le = len(extraArr)
#     print(le)
#     return le
#
#     # print(la)
#     # print(len(extraArr))
#     # print(la - len(extraArr))
#
#
# equalizeArray([3, 3, 2, 1, 3])
# # equalizeArray([1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 8, 8, 8])


def equalizeArray(arr):
    x = 0
    extraArr = []

    for i in arr:
        # 1
        AC = arr.count(i)
        # 2
        if AC >= x:
            x = AC
        elif AC < x:
            extraArr.append(i)
    # 3
    le = len(extraArr)
    print(le)
    return le


#1 we want to loop through the array and count how many there are of each item in the array.
#2 then store the largest number of that count to x, and if it's smaller we append that to another list.
#3 this allows us to count the appended list as our intended result beacuse it's adding to it everything that's not the highest even number.



