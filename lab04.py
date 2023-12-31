"""
Author:         Folu Taiwo
Date:           9/19/23
Assignment:     Lab 04
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION: This a calculator to determine potential final grades for CPSC 1050

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
attendance = str(input()).strip().upper()
#user did not enter y or n
while not (attendance == "Y" or attendance == "N"):
    print("Please input (Y/N)!")
    attendance = str(input()).strip().upper()

#Find the users lab grade
lab_total = 0
min_grade = 0
minimum_lab = 1000
#Did show up to at least 9/10 labs on tuesdays
if (attendance == "Y"):
    print("We will be dropping your lowest lab.")
    for i in range(10):
        print(f"Please input your lab {i + 1} grade (out of 100):")
        lab_grade = float(input())
        lab_total += lab_grade
        if minimum_lab > lab_grade:
            minimum_lab = lab_grade
    lab_total -= minimum_lab        
    lab_avg= lab_total / 9
    print(f"Your lowest lab grade was a {minimum_lab:.2f}, and we dropped your lowest lab so your lab grade is a {lab_avg:.2f}.")
#Did not show up to at least 9/10 labs on tuesdays
else:
    print("We will not dropping your lowest lab.")
    for i in range (10):
        print(f"Please input your lab {i + 1} grade (out of 100):")
        lab_grade = float(input())
        lab_total += lab_grade
    lab_avg = lab_total / 10
    print(f"Your average lab grade is a {lab_avg:.2f}.")
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
    option = str(input()).strip().upper() # a -> A
    while not (option == 'H' or option == 'G' or option == 'S' or option == 'Q'):
        print("Invalid option, please choose a valid option.")
        print("\nPlease choose one of these options:")
        print("H - Highest possible grade with 100 percent Final Exam Score")
        print("G - Grade based on possible Final Exam Score")
        print("S - Score necessary on Final Exam for desired grade")
        print("Q - Quit the program")
        print("Enter your choice:")
        option = str(input()).strip().upper() # a -> A
#Case H
    if option == 'H':
        final_exam_grade = 100
        exam_avg = (exam1_grade+exam2_grade+final_exam_grade)/ 3
        weighted_avg = (0.1*textbook_avg)+(0.1*programming_avg)+(0.1*quiz_avg)+(0.2*project_avg)+(0.2*lab_avg)+(0.3*exam_avg)
        maximum_value = min(exam_avg,weighted_avg)
        if maximum_value >= 89.5:
            highest_letter = 'A'
        elif maximum_value < 89.5 and maximum_value >= 79.5:
            highest_letter = 'B'
        elif maximum_value < 79.5 and maximum_value >= 69.5:
            highest_letter = 'C'
        elif maximum_value < 69.5 and maximum_value >= 59.5:
            highest_letter = 'D'
        elif maximum_value < 59.5:
            highest_letter = 'F'
        
        if lab_avg < 59.5:
            highest_letter = 'F'

        print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
        print(f"Your final weighted score would be {weighted_avg:.2f} and your average exam score would be {exam_avg:.2f}.")
#Case G
    if option == 'G':
        print('Estimate your grade on the final exam:')
        final_exam_grade = float(input())
        while not (final_exam_grade >= 0 and final_exam_grade <= 100):
            print('That does not make any sense. Exiting program. You must make between a 0 and 100.')
            exit(0)
        exam_avg = (exam1_grade+exam2_grade+final_exam_grade)/ 3
        weighted_avg = (0.1*textbook_avg)+(0.1*programming_avg)+(0.1*quiz_avg)+(0.2*project_avg)+(0.2*lab_avg)+(0.3*exam_avg)
        maximum_value = min(exam_avg,weighted_avg)
        if maximum_value >= 89.5:
            highest_letter = 'A'
        elif maximum_value < 89.5 and maximum_value >= 79.5:
            highest_letter = 'B'
        elif maximum_value < 79.5 and maximum_value >= 69.5:
            highest_letter = 'C'
        elif maximum_value < 69.5 and maximum_value >= 59.5:
            highest_letter = 'D'
        elif maximum_value < 59.5:
            highest_letter = 'F'
        
        if lab_avg < 59.5:
            highest_letter = 'F'
        print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
        print(f"Your final weighted score would be {weighted_avg:.2f} and your average exam score would be {exam_avg:.2f}.")
#Case S
    if option == 'S':
        print("What grade do you want to get in the class? (A,B,C,D)")
        desired_grade = str(input()).strip().upper()
        while not (desired_grade == 'A' or desired_grade == 'B' or desired_grade == 'C' or desired_grade == 'D'):
            print("Select A, B, C, or D.")
            print("What grade do you want to get in the class? (A,B,C,D)")
            desired_grade = str(input()).strip().upper()
        if desired_grade == 'A':
            minimum_score = 89.5
        elif desired_grade == 'B':
            minimum_score = 79.5
        elif desired_grade == 'C':
            minimum_score = 69.5
        elif desired_grade == 'D':
            minimum_score = 59.5
        lowest_final = (3*minimum_score)-(exam1_grade+exam2_grade)
        possible_lowest_final = ((minimum_score-(0.1*textbook_avg+0.1*programming_avg+0.1*quiz_avg+0.2*project_avg+0.2*lab_avg))*(3/0.3))-(exam1_grade+exam2_grade)
        max_lowest = max(lowest_final,possible_lowest_final)
        if max_lowest > 100:
            print(f"You can't get that grade because your exam average is not high enough. You would need at least a {max_lowest:.2f}% on the final to get that grade... and that isn't possible.")
            if lab_avg < 59.5:
                print(f"You're failing lab and your exam average is not high enough to get that grade. You would need at least a {max_lowest:.2f}% on the final to get that grade... and that isn't possible.")
        elif max_lowest <= 100:
            if lab_avg < 59.5:
                print("You're failing lab! You will not pass the class.")
            elif lab_avg >= 59.5:
                print(f"Your lowest possible final exam grade to get your desired grade ({desired_grade}) is a {max_lowest:.2f}%")
    
    if option == 'Q':
        break

print(f"Your final weighted score would be {weighted_avg:.2f} and your average exam score would be {exam_avg:.2f}.")
print(f"Your grade would be a {highest_letter} if you got a {final_exam_grade:.2f} on the final.")
print(f"Your final weighted score would be {weighted_avg:.2f} and your average exam score would be {exam_avg:.2f}.")
print("What grade do you want to get in the class? (A,B,C,D)")
print("Select A, B, C, or D.")
print(f"Your lowest possible final exam grade to get your desired grade ({desired_grade}) is a {possible_lowest_final:.2f}%")
print(f"You can't get that grade because your exam average is not high enough. You would need at least a {lowest_final:.2f}% on the final to get that grade... and that isn't possible.")
print(f"You're failing lab and your exam average is not high enough to get that grade. You would need at least a {lowest_final:.2f}% on the final to get that grade... and that isn't possible.")
print("Invalid option, please choose a valid option.")
print("You're failing lab! You will not pass the class.")