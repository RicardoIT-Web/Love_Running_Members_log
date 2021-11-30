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


if fname and lname not in existing_user_fnames:
    WORKSHEET = SHEET.worksheet("members_details")
    WORKSHEET.append_row([fname] + [lname])
if (fname) not in existing_user_fnames:
    if (lname) not in existing_user_lnames:
        SHEET.add_worksheet(fname, 53, 20)
        USER_WORKSHEET = SHEET.worksheet(fname)
        USER_WORKSHEET.update(
            "A1:H1",
            [
                ["Monday"],
                ["Tuesday"],
                ["Wednesday"],
                ["Thursday"],
                ["Friday"],
                ["Saturday"],
                ["Sunday"],
                ["Weekly_Target"]
            ],
            major_dimension="COLUMNS")


def welcome_message():
    """
    Function to welcome user which will include users first name called from
    fname_input function
    """
    print(f"Welcome {fname}!\n")


welcome_message()


answer = input("Would you like to provide a weekly target? y/n: \n")
if answer == "n":
    print(f"OK {fname} Let's move on...\n")
elif answer == "y":
    weekly_target = input("How many KMs do you plan to run per week?\n")


def user_instructions():
    """
    Provide user with guidance of input responses
    """

    print("Please provide the distance of your daily runs. ")
    print("You should provide this data in numerical form. ")
    print("Example: 3.2 = 3.2km run, 5 = 5km run\n")
    print("If you did not run on a particular day, please type 0.\n ")

user_answers = []
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
for weekday in weekdays:
    answer = input(f"How many kms did you run on {weekday}? ")
    while not answer.isnumeric():
        answer = input("Error: please enter a number ")
    user_answers.append(answer)

print(f"you have entered: {user_answers}")
# print(f"your total distance run this week is:" (mon_answer) + (tue_answer) + (wed_answer) + (thu_answer) + (fri_answer) + (sat_answer) + (sun_answer))


def update_members_log(test, weekly_target):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("updating members log...\n")
    members_log_worksheet = SHEET.worksheet(fname)
    members_log_worksheet.append_row(test)
    members_log_worksheet.update_acell("H2", weekly_target)
    print("Members log updated.\n")


def main():
    """
    Run all program functions
    """
    update_members_log(user_answers, weekly_target)


main()
