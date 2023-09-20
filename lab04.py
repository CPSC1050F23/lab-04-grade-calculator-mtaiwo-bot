"""
Author:         Folu Taiwo
Date:           9/19/23
Assignment:     Lab 04
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION:

"""

print("Welcome to the grade calculator for CPSC 1050!")

print("What is your Textbook Activities average?")
TA = float(input())
print("What is your Programming Activities average?")
PA = float(input())
print("What is your Quizzes average?")
Q = float(input())
print("What is your Projects average?")
P = float(input())
print("Did you show up to at least 9/10 labs on Tuesdays this semester? (Y/N)")
did_show_up = str(input()).strip()
#user did not enter y or n
while not (did_show_up == "Y" or did_show_up == "N"):
    print("Please input (Y/N)!")
    did_show_up = str(input()).strip()

#Find the users lab grade
min_grade = 100
num_labs = 10
#Did show up to at least 9/10 labs on tuesdays
if (did_show_up == "Y"):
    print("We will be dropping your lowest lab.")
    for i in range(0,11):
        print(f"Please input your lab {i + 1} grade (out of 100):")
        grade = float(input())
        total_grade = 0
        total_grade += grade
        if min_grade > grade:
            min_grade = grade
            num_labs = i
    total_grade -= min_grade
    lab_avg = total_grade / 10
    print(f"Your lowest lab grade was a {min_grade:.2f}, and we dropped your lowest lab so your lab grade is a {lab_avg:.2f}.")
#Did not show up to at least 9/10 labs on tuesdays
else:
    print("We will not be dropping your lowest lab.")
    for i in range (0,11):
        print(f"Please input your lab {i + 1} grade (out of 100):")
        grade = float(input())
        total_grade = 0
        total_grade += grade
    lab_avg = total_grade / 10
    print(f"Your average lab grade is {total_grade:.2f}")
#Ask user for exam grades
print("What is your first exam grade?")
exam1_grade = float(input())
print("What is your second exam grade?")
exam2_grade = float(input())
#Start the loop
while True:
    print("\nPlease choose one of these options:")
    print("H - Highest possible grade with 100 percent Final Exam Score")
    print("G - Grade based on possible Final Exam Score")
    print("S - Score necessary on Final Exam for desired grade")
    print("Q - Quit the program")

print("Enter your choice:")
option = input().upper().strip() # a -> A
#Case H
if option == 'H':
    final_exam_grade = 100
    exam_avg = ((exam1_grade+exam2_grade+final_exam_grade)/3)
    weighted_avg = (.1(TA)+.1(PA)+.1(Q)+.2(P)+.2(lab_avg)+.3(exam_avg))/(.1+.1+.1+.2+.2+.2+.3)
    highest_letter = 0
    if exam_avg and weighted_avg >= 89.5:
        highest_letter = 'A'
    elif 89.5 >= exam_avg and weighted_avg >= 79.5:
        highest_letter = 'B'
    elif 79.5 >= exam_avg and weighted_avg >= 69.5:
        highest_letter = 'C'
    elif 69.5 >= exam_avg and weighted_avg >= 59.5:
        highest_letter = 'D'
    else:
        highest_letter = 'D'
        print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
        print(f"Your final weighted score would be {weighted_average:.2f} and your average exam score would be {exam_avg:.2f}.")
#Case G
    if option == 'G':
        print("Estimate your grade on the final exam:")
        final_exam_grade = float(input())
        while not (0 <= final_exam_grade <= 100):
            print("That does not make any sense. Exiting program. You must make between a 0 and 100.")
            break
        exam_avg = ((exam1_grade+exam2_grade+final_exam_grade)/3)
        weighted_avg = (.1(TA)+.1(PA)+.1(Q)+.2(P)+.2(lab_avg)+.3(exam_avg))/(.1+.1+.1+.2+.2+.2+.3)  
        highest_letter = 0
        if exam_avg and weighted_avg >= 89.5:
            highest_letter = 'A'
        elif 89.5 >= exam_avg and weighted_avg >= 79.5:
            highest_letter = 'B'
        elif 79.5 >= exam_avg and weighted_avg >= 69.5:
            highest_letter = 'C'
        elif 69.5 >= exam_avg and weighted_avg >= 59.5:
            highest_letter = 'D'
        else:
            highest_letter = 'D'      
        print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
        print(f"Your final weighted score would be {weighted_average:.2f} and your average exam score would be {exam_avg:.2f}.")

print("What grade do you want to get in the class? (A,B,C,D)")
desired_grade = str(input()).upper().strip()
while not (desired_grade == "A" or desired_grade == "B" or desired_grade == "C" or desired_grade == "D"):
    print("Select A, B, C, or D.")
if desired_grade == 'A':
    min_score = 89.5
    possible_lowest_final = final_exam
elif desired_grade == 'B':
    min_score = 79.5
elif desired_grade == 'C':
    min_score = 69.5
else:
    print("You're failing lab! You will not pass the class.")
print(f"Your lowest possible final exam grade to get your desired grade ({desired_grade}) is a {possible_lowest_final:.2f}%")
print(f"You can't get that grade because your exam average is not high enough. You would need at least a {lowest_final:.2f}% on the final to get that grade... and that isn't possible.")
print(f"You're failing lab and your exam average is not high enough to get that grade. You would need at least a {lowest_final:.2f}% on the final to get that grade... and that isn't possible.")

print("Invalid option, please choose a valid option.")