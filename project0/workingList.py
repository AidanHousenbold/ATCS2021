careers = ['programer', 'water polo player', 'teacher', 'driver']
teacherIndex = careers.index('teacher')
print("Index of teacher is ")
print(teacherIndex)
print("teacher" in careers)
careers.append("chef")
careers.insert(0, "baker")
for career in careers:
    print(career)