# average height using for loop
# dont use len() and sum() functions

student_heights = input("enter list of students heights: ").split()
# strings -> convert to int
print(type(student_heights[0]))
# for stud in student_heights:
#     stud = int(stud)
##  did not work

for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i]) ## works
print(type(student_heights[0]))


# finding average without using len() and sum()
count = 0
total = 0
for stud in student_heights:
    count += 1
    total += stud
# print(f"the average height is : {round(total/count)}")
# or 
print(f"the average height is : {(total//count)}")