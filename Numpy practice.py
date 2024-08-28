# import numpy as np
# from numpy import random

# a=np.array([1,2,3,4])
# print(a)

n = int(input())
student_marks = {}
for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()

sum_marks=sum(student_marks[query_name])
len_marks=len(student_marks[query_name])
average=sum_marks/len_marks
print(f"{average:.2f}")

