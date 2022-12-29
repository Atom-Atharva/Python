# marks is a list
marks = [1, 2, 3, 4, 5, "atharva"]
print(marks)
print(marks[5])

# Minus represent Iteration from last--
print(marks[-1])

#Print in range
print(marks[0:4])

for score in marks:
    print(score)


marks.append(6)
marks.insert(0, 7)

print(marks)

print(4 in marks)
print(8 in marks)

print(len(marks))


i=0

while(i<len(marks)):
    print(marks[i])
    i=i+1