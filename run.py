import webbrowser
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


def welcome_members_message():
    """
    A welcome message to the member
    """
    print("Welcome to the Love Running Members Log\n")


welcome_members_message()


def fname_input(prompt):
    """
    Function to promt user to input first name
    """
    return input(prompt)

# Message to user prompting input of fname and validate it's an alpha response


fname = fname_input("Hello Member!\nPlease type your first name: \n")
while not fname.isalpha():
    fname = input("Error: please enter a First Name ")


def lname_input(prompt):
    """
    Function to promt user to input last name
    """
    return input(prompt)

# Message to user prompting input of lname and validate it's an alpha response


lname = lname_input("Please type your last name: \n")
while not lname.isalpha():
    lname = input("Error: please enter a last Name ")


# Identify members details tab and search if names already exist
# If so, add data to existing members tab. if not, create new tab

WORKSHEET = SHEET.worksheet("members_details")
existing_user_fnames = WORKSHEET.col_values(1)
existing_user_lnames = WORKSHEET.col_values(2)

if fname not in existing_user_fnames:
    WORKSHEET = SHEET.worksheet("members_details")
    WORKSHEET.append_row([fname] + [lname])

if (fname) not in existing_user_fnames:
    SHEET.add_worksheet(fname, 53, 20)
    USER_WORKSHEET = SHEET.worksheet(fname)
    USER_WORKSHEET.update(
        "A1:I1",
        [
            ["Monday"],
            ["Tuesday"],
            ["Wednesday"],
            ["Thursday"],
            ["Friday"],
            ["Saturday"],
            ["Sunday"],
            ["Weekly Target"],
            ["BMI"]
        ],
        major_dimension="COLUMNS")


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
    print("Example: 3.2 = 3.2km run, 5.0 = 5km run\n")
    print("If you did not run on a particular day, please type 0.\n ")


user_instructions()


# Define user answers as empty array for user input to be appended
# in each iteration
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
    answer = input(f"How many kms did you run on {weekday}? \n")
    while True:
        try:
            float(answer)
            break
        except TypeError as e:
            answer = input(f"{e}: {answer} is not a number! Try Again")
    user_answers.append(float(answer))

print(f"you have entered: {user_answers}\n")

# calculate total weekly distance run
sums = user_answers
print(f"Your total distance this week is: {sum(sums)}kms \n")


def update_distance_log(weekday_answers):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("Let's get these runs logged...\n")
    members_log_worksheet = SHEET.worksheet(fname)
    members_log_worksheet.append_row(weekday_answers)
    print("Members log updated.\n")


update_distance_log(user_answers)


# prompt user is they'd like to provide a weekly distance target

weekly_target = input("Would you like to provide a weekly target? y/n: \n")
if weekly_target == 'n':
    print(f"OK {fname} Let's move on...\n")
elif weekly_target == "y":
    last_target = SHEET.worksheet(fname).acell("H2").value
    print(f"Your last Target was: {last_target} km \n")
    weekly_target = input("How many KMs do you plan to run per week?\n")


# Prompt user if they'd like to calculate BMI and reveal calculated result
bmi_data = input(f"{fname} Would you like to know what your BMI is? y/n: \n")
if bmi_data == "n":
    print(f"OK {fname} Let's move on...\n")

elif bmi_data == "y":
    height = float(input("Please enter your current height in cm: \n"))
    weight = float(input("Please enter your current weight in kg: \n"))
    bmi_data = weight/(height/100)**2
    print(f"Your BMI is currently {bmi_data} \n")
    print("To find out more about BMI and how it is meassured; \n")
    print("Please select option below: \n")

    bmi_info = input(
        "Want to know more about BMI & how it's calculated? y/n \n")
    if bmi_info == "n":
        print(f"OK {fname} Let's move on...\n")

    elif bmi_info == "y":
        webbrowser.open(
            "https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/")


def update_other_data(weekly_target_data):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("updating members log...\n")
    members_log_worksheet = SHEET.worksheet(fname)
    members_log_worksheet.update_acell("H2", weekly_target_data)
    members_log_worksheet.update_acell("I2", bmi_data)
    print("Members log updated.\n")
    print("Thank you for using Members Log.\n")
    print("Come back next week and log those runs again.")


update_other_data(weekly_target)
