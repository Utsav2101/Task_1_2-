import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "contact_number", "email_id"])

        writer.writerow(info_list)



if __name__ == '__main__' :
    condition = True
    student_num = 1
    while condition :
        student_info = input("Enter the student info for student #{} in the following format(Name Age contact_number Email_id): ".format(student_num))

        student_info_list = student_info.split(' ')

        print("\n The entered information is -\n NAme : {}\n Age: {} \n contact_number: {} \n email_id: {}"
        .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check input("Is the entered info correct? (Yes/No):")


        if choice_check == "Yes":
                write_info_csv(student_info_list)



                condition_check_input = input(" Enter (Yes/ No) to want another student info :")
                if condition_check_input == "Yes":
                    condition = True
                    student_num = student_num + 1
                elif condition_check_input == "No":
                    condition = False
                elif choice_check == "No"
                    print("\n Please re-enter the values!")

