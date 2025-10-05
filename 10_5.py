# 1 

# solve diagnol difference in hackerrank's python

# def diagonalDifference(arr):
#     n = len(arr)
#     left_to_right = 0
#     right_to_left = 0
    
#     for i in range(n):
#         left_to_right += arr[i][i]
#         right_to_left += arr[i][n - 1 - i]

#     return abs(left_to_right - right_to_left) 


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())
#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')
#     fptr.close()











# 2 

# "solve me first" in hackerrank's python

# def solveMeFirst(a,b):
# 	return a + b


# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)









# 3 

# simple array sum in hackerrank's python
# def simpleArraySum(ar):
#     # Write your code here
#     total_sum = sum(ar)
#     return total_sum

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()










# 4 

# compare triplets in hackerrank's python
# def compareTriplets(a, b):

#     # Write your code here
#     a_score = 0
#     b_score = 0
    
#     for i in range(3):
#         if a[i] > b[i]:
#             a_score += 1
#         elif a[i] < b[i]:
#             b_score += 1
#     return (a_score, b_score)









# 5 

# very big sum in hackerrank's python

# def aVeryBigSum(ar):
#     # Write your code here
#     long = sum(ar)
#     return long

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = aVeryBigSum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()










# # 6 
# 
# mini max sum
# def miniMaxSum(arr):
#     # Write your code here
#     totalSum = sum(arr)
#     minSum = totalSum - max(arr)
#     maxSum = totalSum - min(arr)
#     print(minSum, maxSum)
    

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)








# 7 
# birthdayCakeCandles in hackerrank's python

# def birthdayCakeCandles(candles):
#     # Write your code here
#     max_candles = max(candles)
#     count_tallest = candles.count(max_candles)
#     return count_tallest
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     candles_count = int(input().strip())

#     candles = list(map(int, input().rstrip().split()))

#     result = birthdayCakeCandles(candles)

#     fptr.write(str(result) + '\n')

#     fptr.close()