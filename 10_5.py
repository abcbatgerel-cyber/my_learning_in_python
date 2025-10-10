# 1

# "solve me first" in hackerrank's python

# def solveMeFirst(a,b):
# 	return a + b

# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)





# 2
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





# 3

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






# 4
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






# 5
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






# 6
# plus minus in hackerrank

# def plusMinus(arr):
#     # Write your code here
#     num = len(arr)
#     positive = 0
#     negative = 0
#     zero = 0
#     for num in arr:
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1
#         else:
#             zero += 1
        
#     print(f"{positive/n:.6f}")
#     print(f"{negative/n:.6f}")
#     print(f"{zero/n:.6f}")


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)






# 7
# timeConversion in hackerrank
# def timeConversion(s):
#     # Цаг, минут, секунд, AM/PM салгах
#     hour = int(s[:2])
#     minute = int(s[3:5])
#     second = int(s[6:8])
#     period = s[8:]  # "AM" эсвэл "PM"
    
#     if period == "AM":
#         if hour == 12:
#             hour = 0
#     else:  # PM
#         if hour != 12:
#             hour += 12
    
#     return "{:02}:{:02}:{:02}".format(hour, minute, second)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()









# 8 
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








# 9
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