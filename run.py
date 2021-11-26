import gspread
from google.oauth2.service_account import Credentials
# from pprint import pprint


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
    fname = input("Error: please enter a last Name ")


def welcome_message():
    """
    Function to welcome user which will include users first name called from
    fname_input function
    """
    print(f"Welcome {fname}!\n")


welcome_message()


# target_run = target_data_input("would you like to provide a weekly target? y/n: ")
# while target_run ==  "y":
#     print("Please provide your weekly target: ")
# else:
#     target_run == "n"
#     print("OK, lets move on...")


def user_instructions():
    """
    Provide user with guidance of input responses
    """

    print("Please provide the distance of your daily runs. ")
    print("You should provide this data in numerical form. ")
    print("Example: 3.2 = 3.2km run, 5 = 5km run\n")
    print("If you did not run on a particular day, please type 0.\n ")


user_instructions()


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


user_answers = [int(mon_answer), int(tue_answer), int(wed_answer), int(thu_answer), int(fri_answer), int(sat_answer), int(sun_answer)]
print(f"you have entered: {user_answers}")


def update_members_log(user_output):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("updating members log...\n")
    members_log_worksheet = SHEET.worksheet(fname)
    members_log_worksheet.update('A2:G2', user_output)
    print("Members log updated.\n")


def main():
    """
    Run all program functions
    """
    update_members_log(user_answers)


main()
