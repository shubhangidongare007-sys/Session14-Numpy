import numpy as np

marks=np.random.randint(30,101,(10,5))

print("Student Marks")
print(marks)

total=marks.sum(axis=1)
average=marks.mean(axis=1)

print("Total Marks")
print(total)

print("Average Marks")
print(average)

print("Highest Total Student:",total.argmax())
print("Lowest Total Student:",total.argmin())

print("Class Mean:",marks.mean())
print("Class Standard Deviation:",marks.std())

reshape_marks=marks.reshape(5,10)

print("Reshaped Array")
print(reshape_marks)

print("Top 3 Students Marks")
top3=np.argsort(total)[-3:]
print(marks[top3])