 #Find the Runner-Up Score!

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format 
# The first line contains N. The second line contains an array A[] of N integers each separated by a space.

# Constraints
# 2 <= N <= 10
# -100 <= A[i] <= 100

# Output Format 
# Output the value of the second largest number.



if __name__ == '__main__':
    n = int(raw_input())
    l = list(map(int, raw_input().split()))
    s = set(l) #to get all the unique numbers
    result = sorted(list(s))
    print(result[-2])
    