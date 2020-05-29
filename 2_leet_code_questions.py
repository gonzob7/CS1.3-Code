import random

# BEST CASE TIME COMPLEXITY: O(n) depending on size of range
# def selfDividingNumbers(left: int, right: int):
#     def valid(num):
#         num = str(num)
#
#         if "0" in num:
#             return False
#
#         for i in range(len(num)):
#             if int(num) % int(num[i]) is not 0:
#                 return False
#         else:
#             return True
#
#     perfect_nums = []
#
#     for i in range(left,right+1):
#         if valid(i):
#             perfect_nums.append(i)
#
#     return perfect_nums
#
#
# # BEST CASE TIME COMPLEXITY: O(n) depending on size of array
# def sortedSquares(A):
#     left_index = 0
#     right_index = len(A) - 1
#
#     ans = []
#
#     while left_index <= right_index:
#         if abs(A[left_index]) > abs(A[right_index]):
#             sqr = A[left_index]**2
#             ans.append(sqr)
#             left_index +=1
#         else:
#             sqr = A[right_index]**2
#             ans.append(sqr)
#             right_index -=1
#
#     return ans[::-1]


def functionName():

    roll = [random.randint(5,6),random.randint(5,6),random.randint(5,6),random.randint(5,6),random.randint(5,6)]
    roll2 = [random.randint(5,6) for x in range(6)]
    print(roll)
    print(roll2)


if __name__ == '__main__':
    functionName()
    # print(selfDividingNumbers(1,100))
    # print(sortedSquares([-4,-1,0,3,10]))
