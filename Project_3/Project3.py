#Student report card management

# Grade: based on percentage
# Pass/Fail is based on individul 's subject marks

names = []
rolls = []
dccn_marks  = []
dbe_marks  = []
python_marks = []
java_marks = []
maths_marks = []
totals = []
percentages = []

num_of_stu = 0

while True:
    print(" === Student Report Card === \n")
    print("1. Add students")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Class Topper")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        num_of_stu = int(input("Enter number of students you want to add: "))

        for i in range(num_of_stu):
            name = input("Enter name: ")
            names.append(name)

            roll = int(input("Enter roll: "))
            rolls.append(roll)

            m1 =  int(input("Enter marks of DCCN: "))
            dccn_marks.append(m1)

            m2 =  int(input("Enter marks of DBE: "))
            dbe_marks.append(m2)

            m3 =  int(input("Enter marks of PYTHON: "))
            python_marks.append(m3)

            m4 =  int(input("Enter marks of JAVA: "))
            java_marks.append(m4)

            m5 =  int(input("Enter marks of MATHS: "))
            maths_marks.append(m5)

            total = m1+m2+m3+m4+m5
            totals.append(total)

            percentage = total/5
            percentages.append(percentage)


    elif ch == 2:
        
        if len(names) == 0:
            print("\nNo student record found.\n")
        else:
            print("=" * 35)
            print("   STUDENTS DETAILS ")
            print("=" * 35)
            for i in range(len(names)):

                #grading 
                if 90 <= percentages[i] <= 100:
                    grade = "A+"
                elif 80 <= percentages[i] < 90:
                    grade = "A"
                elif 70 <= percentages[i] < 80:
                    grade = "B"
                elif 60 <= percentages[i] < 70:
                    grade = "C"
                elif 40 <= percentages[i] < 60:
                    grade = "D"
                else:
                    grade = "F"

                if (python_marks[i] < 33 or
                    java_marks[i] < 33 or
                    maths_marks[i] < 33 or
                    dbe_marks[i] < 33 or
                    dccn_marks[i] < 33):
                    status = "FAIL"
                else:
                    status = "PASS"

                print("Name       :", names[i])
                print("Roll No    :", rolls[i])
                print("DCCN       :", dccn_marks[i])
                print("DBE        :", dbe_marks[i])
                print("Python     :", python_marks[i])
                print("Java       :", java_marks[i])
                print("Maths      :", maths_marks[i])
                print("Total      :", totals[i])
                print("Percentage :", percentages[i], "%")
                print("Grade      :", grade)
                print("Status     :", status)
                print("-" * 35)

    elif ch == 3:

        if len(names) == 0:
            print("No student records found.")
            continue

        else:
            found = False

        print("1. Search by Roll Number")
        print("2. Search by Name")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            srch = int(input("Enter roll number: "))

            for i in range(len(names)):
                if srch == rolls[i]:
                    found = True

                    # grading
                    if 90 <= percentages[i] <= 100:
                        grade = "A+"
                    elif 80 <= percentages[i] < 90:
                        grade = "A"
                    elif 70 <= percentages[i] < 80:
                        grade = "B"
                    elif 60 <= percentages[i] < 70:
                        grade = "C"
                    elif 40 <= percentages[i] < 60:
                        grade = "D"
                    else:
                        grade = "F"

                    # status
                    if (python_marks[i] < 33 or
                        java_marks[i] < 33 or
                        maths_marks[i] < 33 or
                        dbe_marks[i] < 33 or
                        dccn_marks[i] < 33):
                        status = "FAIL"
                    else:
                        status = "PASS"

                    print("Name       :", names[i])
                    print("Roll No    :", rolls[i])
                    print("DCCN       :", dccn_marks[i])
                    print("DBE        :", dbe_marks[i])
                    print("Python     :", python_marks[i])
                    print("Java       :", java_marks[i])
                    print("Maths      :", maths_marks[i])
                    print("Total      :", totals[i])
                    print("Percentage :", percentages[i], "%")
                    print("Grade      :", grade)
                    print("Status     :", status)
                    print("-" * 35)

        elif choice == 2:
            srch = input("Enter Name: ")

            for i in range(len(names)):
                if srch.lower() == names[i].lower():
                    found = True

                    # grading
                    if 90 <= percentages[i] <= 100:
                        grade = "A+"
                    elif 80 <= percentages[i] < 90:
                        grade = "A"
                    elif 70 <= percentages[i] < 80:
                        grade = "B"
                    elif 60 <= percentages[i] < 70:
                        grade = "C"
                    elif 40 <= percentages[i] < 60:
                        grade = "D"
                    else:
                        grade = "F"

                    # status
                    if (python_marks[i] < 33 or
                        java_marks[i] < 33 or
                        maths_marks[i] < 33 or
                        dbe_marks[i] < 33 or
                        dccn_marks[i] < 33):
                        status = "FAIL"
                    else:
                        status = "PASS"

                    print("Name       :", names[i])
                    print("Roll No    :", rolls[i])
                    print("DCCN       :", dccn_marks[i])
                    print("DBE        :", dbe_marks[i])
                    print("Python     :", python_marks[i])
                    print("Java       :", java_marks[i])
                    print("Maths      :", maths_marks[i])
                    print("Total      :", totals[i])
                    print("Percentage :", percentages[i], "%")
                    print("Grade      :", grade)
                    print("Status     :", status)
                    print("-" * 35)

        else:
            print("Invalid Search Choice")

        if not found:
            print("Student Not Found")

    elif ch == 4:

        if len(names) == 0:
            print("No student records found.")

        else:
            topper = 0

            for i in range(len(names)):
                if percentages[i] > percentages[topper]:
                    topper = i

            print("Topper :", names[topper])
            print("Percentage :", percentages[topper], "%")
            
    elif ch == 5:
        print("Thank You!")
        break

    elif ch < 1 or ch > 5:
        print("Invalid Choice")







