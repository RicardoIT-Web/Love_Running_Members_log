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
        pass
    mon_answer = input("How many kms did you run on Monday? ")
    if mon_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    if weekday == "Tuesday":
        pass
    tue_answer = input("How many kms did you run on Tuesday? ")
    if tue_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    if weekday == "Wednesday":
        pass
    wed_answer = input("How many kms did you run on Wednesday? ")
    if wed_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    if weekday == "Thursday":
        pass
    thu_answer = input("How many kms did you run on Thursday? ")
    if thu_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    if weekday == "Friday":
        pass
    fri_answer = input("How many kms did you run on Friday? ")
    if fri_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    if weekday == "Saturday":
        pass
    sat_answer = input("How many kms did you run on Saturday? ")
    if sat_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    if weekday == "Sunday":
        pass
    sun_answer = input("How many kms did you run on Sunday? ")
    if sun_answer <= "-1":
        print("Invalid entry. If you've not had a run on this day, please type 0.")
        continue
    break


user_answers = mon_answer, tue_answer, wed_answer, thu_answer, fri_answer, sat_answer, sun_answer
print(f"Your daily distances for this week are {user_answers}")


# def validate_data(user_answers):
#     """
#     Function for validating User output data
#     """
#     try:
#         if user_answers = :
#         raise ValueError(
#                 f"7 values required, you only provided {len(user_answers)}"
#             )
#     except ValueError as e:
#         print(f"Invalid data: {e}, please try again.\n")

#     return user_answers


# validate_data(user_answers)
