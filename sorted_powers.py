def sortedSquares(A: [int]):
    left_index = 0
    right_index = len(A) - 1

    ans = []

    while left_index <= right_index:
        if abs(A[left_index]) > abs(A[right_index]):
            sqr = A[left_index]**2
            ans.append(sqr)
            left_index +=1
        else:
            sqr = A[right_index]**2
            ans.append(sqr)
            right_index -=1

    return ans[::-1]


if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10])
