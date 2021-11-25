"""
Link to google spreadsheet.
"""
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
lname = lname_input("Please type your last name: \n")


def welcome_message():
    """
    Function to welcome user which will include users first name called from
    fname_input function
    """
    print(f"Welcome {fname}!\n")


welcome_message()


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


user_answers = mon_answer, tue_answer, wed_answer, thu_answer, fri_answer, sat_answer, sun_answer


# calc_bmi = input('Would you like to monitor your BMI? (y/n): \n')

# if calc_bmi == "y":
#     bmi_weight = input("Please provide your current weight in kg: ")
#     if bmi_weight <= "0":
#         print("Invalid Entry, Please try again")
# else:
#     pass

# if bmi_height = input("Please provide your height in cm: ")
# validate_data(user_answers)
