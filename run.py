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
    return input(prompt)


def lname_input(prompt):
    return input(prompt)


fname = fname_input("Input your first name: ")
lname = lname_input("Input your last name: ")


def welcome_message():
    print(f"Welcome {fname}!\n")


welcome_message()


def user_instructions():

    print("Please provide the distance of your runs. ")
    print("You should provide this data in numerical form. ")
    print("Example: 3.2 = 3.2kms run, 5 = 5kms run\n")
    print("If you did not run on a particular day, please type 0.\n ")


user_instructions()


weekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
for weekday in weekdays:
    if weekday == "Monday":
        pass
    input("How many kms did you run on Monday? ")
    if weekday == "Tuesday":
        pass
    input("How many kms did you run on Tuesday? ")
    if weekday == "Wednesday":
        pass
    input("How many kms did you run on Wednesday? ")
    if weekday == "Thursday":
        pass
    input("How many kms did you run on Thursday? ")
    if weekday == "Friday":
        pass
    input("How many kms did you run on Friday? ")
    if weekday == "Saturday":
        pass
    input("How many kms did you run on Saturday? ")
    if weekday == "Sunday":
        input("How many kms did you run on Sunday? ")

    exit()
# def get_distance_run_data():
#     """
#     Recieve daily kms run from members.
#     """

#     dist_str_mon = input("Enter Monday's distance here: ")
#     print(f"The distance provided for Monday's run is {dist_str_mon}kms\n")

#     dist_str_tues = input("Enter Tuesday's distance here: ")
#     print(f"The distance provided for Tuesday's run is {dist_str_tues}kms\n")

#     dist_str_wed = input("Enter Wednesday's distance here: ")
#     print(f"The distance provided for Wednesday's run is {dist_str_wed}kms\n")

#     dist_str_thur = input("Enter Thursday's distance here: ")
#     print(f"The distance provided for Thursday's run is {dist_str_thur}kms\n")

#     dist_str_fri = input("Enter Friday's distance here: ")
#     print(f"The distance provided for Friday's run is {dist_str_fri}kms\n")

#     dist_str_sat = input("Enter Saturday's distance here: ")
#     print(f"The distance provided for Saturday's run is {dist_str_sat}kms\n")

#     dist_str_sun = input("Enter Sunday's distance here: ")
#     print(f"The distance provided for Sunday's run is {dist_str_sun}kms\n")

#     distance_data = dist_str_mon.split(","), dist_str_tues.split(","), dist_str_wed.split(","), dist_str_thur.split(","), dist_str_fri.split(","), dist_str_sat.split(","), dist_str_sun.split(",")
#     validate_data(distance_data)


# def validate_data(input):
#     """
#     Try
#     """
#     try:
#         if len(input) != 7:
#             raise ValueError(
#                 f"7 values required, you only provided {len(input)}"
#             )
#     except ValueError as e:
#         print(f"Invalid data: {e}, please try again.\n")

#     print(input)


# get_distance_run_data()
