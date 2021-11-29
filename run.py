import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_running_members_log")


def fname_input(prompt):
    """
    Function to promt user to input first name
    """
    return input(prompt)


def lname_input(prompt):
    """
    Function to promt user to input last name
    """
    return input(prompt)


fname = fname_input("Hello Member!\nPlease type your first name: \n")
while not fname.isalpha():
    fname = input("Error: please enter a First Name ")

lname = lname_input("Please type your last name: \n")
while not lname.isalpha():
    lname = input("Error: please enter a last Name ")


SHEET = GSPREAD_CLIENT.open("love_running_members_log")

WORKSHEET = SHEET.worksheet("members_details")

existing_user_fnames = WORKSHEET.col_values(1)
existing_user_lnames = WORKSHEET.col_values(2)


if (fname) not in existing_user_fnames:
    if (lname) not in existing_user_lnames:
        WORKSHEET.insertRow = [fname] + [lname]
        SHEET.add_worksheet(fname, 53, 20)
        USER_WORKSHEET = SHEET.worksheet(fname)
        USER_WORKSHEET.update(
            "A1:G1",
            [
                ["Monday"],
                ["Tuesday"],
                ["Wednesday"],
                ["Thursday"],
                ["Friday"],
                ["Saturday"],
                ["Sunday"]
            ],
            major_dimension="COLUMNS")


def welcome_message():
    """
    Function to welcome user which will include users first name called from
    fname_input function
    """
    print(f"Welcome {fname}!\n")


welcome_message()


def user_weekly_target():
    """
    Asks the user if they'd like to monitor
    their weekly targets to allow the application
    to provide a performance summary at the end of the week.
    """
    target_answer = input("Would you like to provide a weekly target? y/n: \n")
    if target_answer == "No" or "no" or "n":
        print("OK... Let's move on...\n")
    elif target_answer == "yes" or "y" or "Y":
        input("How many KMs do you plan to run per week?\n")


user_weekly_target()


def user_instructions():
    """
    Provide user with guidance of input responses
    """

    print("Please provide the distance of your daily runs. ")
    print("You should provide this data in numerical form. ")
    print("Example: 3.2 = 3.2km run, 5 = 5km run\n")
    print("If you did not run on a particular day, please type 0.\n ")


user_instructions()

# days = 0
# week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# while days < 7:
#     mon_answer = input("How many Km did you run on " + week[days] + ": ")
#     if mon_answer.isdigit():
#         print("For " + week[days] + " You have entered: " + (mon_answer))
#         if mon_answer.isalpha():
#             print("Invalid entry. Please type a number")
#             continue
#         days += 1
#     tue_answer = input("How many Km did you run on " + week[days] + ": ")
#     if tue_answer.isdigit():
#         print("For " + week[days] + " You have entered: " + (tue_answer))
#         if tue_answer.isalpha():
#             print("Invalid entry. Please type a number")
#         days += 1
#     break
# print(int[mon_answer, tue_answer])


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for weekday in weekdays:
    if weekday == "Monday":
        mon_answer = input("How many kms did you run on Monday? ")
        while not mon_answer.isnumeric():
            mon_answer = input("Error: please enter a number ")
        continue

    if weekday == "Tuesday":
        tue_answer = input("How many kms did you run on Tuesday? ")
        while not tue_answer.isnumeric():
            tue_answer = input("Error: please enter a number ")
            if tue_answer.isdigit():
                tue_answer = int(tue_answer)
        continue

    if weekday == "Wednesday":
        wed_answer = input("How many kms did you run on Wednesday? ")
        while not wed_answer.isnumeric():
            wed_answer = input("Error: please enter a number ")
        continue

    if weekday == "Thursday":
        thu_answer = input("How many kms did you run on Thursday? ")
        while not thu_answer.isnumeric():
            thu_answer = input("Error: please enter a number ")
        continue

    if weekday == "Friday":
        fri_answer = input("How many kms did you run on Friday? ")
        while not fri_answer.isnumeric():
            fri_answer = input("Error: please enter a number ")
        continue

    if weekday == "Saturday":
        sat_answer = input("How many kms did you run on Saturday? ")
        while not sat_answer.isnumeric():
            sat_answer = input("Error: please enter a number ")
        continue

    if weekday == "Sunday":
        sun_answer = input("How many kms did you run on Sunday? ")
        while not sun_answer.isnumeric():
            sun_answer = input("Error: please enter a number ")
        continue
    break


user_answers = [mon_answer, tue_answer, wed_answer, thu_answer, fri_answer, sat_answer, sun_answer]
print(f"you have entered: {user_answers}")


def update_members_log(user_answers):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("updating members log...\n")
    members_log_worksheet = SHEET.worksheet(fname)
    members_log_worksheet.append_row(user_answers)
    print("Members log updated.\n")


def main():
    """
    Run all program functions
    """
    update_members_log(user_answers)


main()
