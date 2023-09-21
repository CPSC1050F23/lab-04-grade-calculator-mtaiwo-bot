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
textbook_avg = float(input())
print("What is your Programming Activities average?")
programming_avg = float(input())
print("What is your Quizzes average?")
quiz_avg = float(input())
print("What is your Projects average?")
project_avg = float(input())
print("Did you show up to at least 9/10 labs on Tuesdays this semester? (Y/N)")
did_show_up = str(input()).strip().upper()
#user did not enter y or n
while not (did_show_up == "Y" or did_show_up == "N"):
    print("Please input (Y/N)!")
    did_show_up = str(input()).strip()

#Find the users lab grade
min_grade = 1000
num_labs = 10
total_grade = 0
#Did show up to at least 9/10 labs on tuesdays
if (did_show_up == "Y"):
    print("We will be dropping your lowest lab.")
    for i in range(10):
        print(f"Please input your lab {i + 1} grade (out of 100):")
        lab_grade = float(input())
        total_grade += lab_grade
        if min_grade > lab_grade:
            min_grade = lab_grade
            num_labs - 1
            total_grade -= min_grade
            lab_avg = total_grade / 9     
    print(f"Your lowest lab grade was a {min_grade:.2f}, and we dropped your lowest lab so your lab grade is a {lab_avg:.2f}.")
#Did not show up to at least 9/10 labs on tuesdays
else:
    print("We will not dropping your lowest lab.")
    for i in range (10):
        print(f"Please input your lab {i + 1} grade (out of 100):")
        lab_grade = float(input())
        total_grade += lab_grade
        lab_avg = total_grade / 10
    print(f"Your average lab grade is {lab_avg:.2f}")
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
        exam_avg = (exam1_grade+exam2_grade+final_exam_grade)/3
        weighted_avg = (TA*0.1)+PA*0.1+Q*0.1+P*0.2+lab_avg*0.2+exam_avg*0.3/(0.1+0.1+0.1+0.2+0.2+0.2+0.3)
        highest_letter = 0
        if exam_avg and weighted_avg >= 89.5:
            highest_letter = 'A'
        elif 89.5 >= exam_avg and weighted_avg >= 79.5:
            highest_letter = 'B'
        elif 79.5 >= exam_avg and weighted_avg >= 69.5:
            highest_letter = 'C'
        else:
            highest_letter = 'D'
        print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
        print(f"Your final weighted score would be {weighted_avg:.2f} and your average exam score would be {exam_avg:.2f}.")
#Case G
    elif option == 'G':
        print("Estimate your grade on the final exam:")
        final_exam_grade = float(input())
        while not (0 <= final_exam_grade <= 100):
            print("That does not make any sense. Exiting program. You must make between a 0 and 100.")
            break
        exam_avg = (exam1_grade+exam2_grade+final_exam_grade)/3
        weighted_avg = (TA*0.1)+PA*0.1+Q*0.1+P*0.2+lab_avg*0.2+exam_avg*0.3/(0.1+0.1+0.1+0.2+0.2+0.2+0.3)
        highest_letter = 0
        if exam_avg and weighted_avg >= 89.5:
            highest_letter = 'A'
        elif 89.5 >= exam_avg and weighted_avg >= 79.5:
            highest_letter = 'B'
        elif 79.5 >= exam_avg and weighted_avg >= 69.5:
            highest_letter = 'C'
        else:
            highest_letter = 'D'
        print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
        print(f"Your final weighted score would be {weighted_avg:.2f} and your average exam score would be {exam_avg:.2f}.")
#Case S
    elif option == 'S':
        print("What grade do you want to get in the class? (A,B,C,D)")
        desired_grade = str(input()).upper().strip()
        while not (desired_grade == "A" or desired_grade == "B" or desired_grade == "C" or desired_grade == "D"):
            print("Select A, B, C, or D.")
        desired_grade = str(input()).upper().strip()
        def calculate_minimum_final_exam_score(desired_grade):
            min_scores = {
                'A': 89.5,
                'B': 79.5,
                'C': 69.5,
                'D': 59.5
            }
            exams_average_score = 3 * desired_grade - (exam1_grade+exam2_grade)
            weighted_average_score = 4 * desired_grade - ((TA*0.1)+PA*0.1+Q*0.1+P*0.2+lab_avg*0.2+exam_avg*0.3/(0.1+0.1+0.1+0.2+0.2+0.2+0.3))
            possible_lowest_final = max(exams_average_score, weighted_average_score)
            return possible_lowest_final
            print(f"Your lowest possible final exam grade to get your desired grade ({desired_grade}) is a {possible_lowest_final:.2f}%")
            if weighted_average_score > exams_average_score:
                print(f"You can't get that grade because your exam average is not high enough. You would need at least a {lowest_final:.2f}% on the final to get that grade... and that isn't possible.")
            else:
                print(f"You're failing lab and your exam average is not high enough to get that grade. You would need at least a {lowest_final:.2f}% on the final to get that grade... and that isn't possible.")

#Case Q
    elif option == 'Q':
        break
#Invalid case
    else:
        print("Invalid option, please choose a valid option.")
        continue
print("You're failing lab! You will not pass the class.")