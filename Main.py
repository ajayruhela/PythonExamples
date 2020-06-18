# program to display student's marks from record
student_name = 'asd'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
i=0
for student in marks:
    print(i)
    i+=1
    
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
