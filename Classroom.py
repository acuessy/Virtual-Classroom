#keep track with the number of students

students = []

while True:
    option = input("Enter a command:")
    if option == 'add' :
        student = input("Enter student:")
        students.append(student)
    if option == 'remove':
        student = input("Remove student: ")
        students.remove(student)
    if option == 'save' :
        name = input("Open file: ")
        file = open(name, "w")
        for student in students:
            file.write(student)
            file.write("\n")
        file.close()
    if option == 'quit':
        break
    if option == "load" :
        name = input("Load file:")
        file = open(name, "r")
        data = file.read()
        file.close()
        contents = data.split("\n")
        students = []
        for student in contents:
            if len(student)>0:
                students.append(student)
    print(students)

# \n is to delimit the data
# think of files as fridges, we want to close them asap

# CLI Command Line Interface/Script/app
