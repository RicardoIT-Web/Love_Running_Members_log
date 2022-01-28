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


def fname_input(prompt):
    """
    Function to prompt user to input first name
    """
    return input(prompt)


def lname_input(prompt):
    """
    Function to prompt user to input last name
    """
    return input(prompt)


def welcome_message(fname):
    """
    Function to welcome user which will include users first name called from
    fname_input function
    """
    print(f"Welcome {fname}!\n")


def user_instructions():
    """
    Provide user with guidance of input responses
    """

    print("Please provide the distance of your daily runs. ")
    print("You should provide this data in numerical form. ")
    print("Example: 3.2 = 3.2km run, 5 = 5km run\n")
    print("If you did not run on a particular day, please type 0.\n ")


def update_distance_log(weekday_answers, fname, lname):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("Let's get these runs logged...\n")
    members_log_worksheet = SHEET.worksheet(f"{fname}{lname}")
    members_log_worksheet.append_row(weekday_answers)
    print("Members log updated.\n")


def update_other_data(weekly_target_data, fname, lname, bmi_data):
    """
    Updating members log to the worksheet.
    Adding a new row with the list data provided
    """
    print("updating members log...\n")
    members_log_worksheet = SHEET.worksheet(f"{fname}{lname}")
    if weekly_target_data != 'n':
        members_log_worksheet.update_acell("H2", weekly_target_data)
    if bmi_data != 'n':
        members_log_worksheet.update_acell("I2", bmi_data)
    print("Members log updated.\n")
    print("Thank you for using Members Log.\n")
    print("Come back next week and log those runs again.")


def main():
    """
    Main function
    """

    welcome_members_message()


# Message to user prompting input of fname and validate an alpha response
    fname = input("Hello Member!\nPlease type your first name: \n")
    fname = fname.upper()
    while not fname.isalpha():
        fname = input("Error: please enter a first name: ")
        fname = fname.upper()

# Message to user prompting input of lname and validate an alpha response
    lname = input("Please type your last name: \n")
    lname = lname.upper()
    while not lname.isalpha():
        lname = input("Error: please enter a last Name: ")
        lname = lname.upper()

# If statement Identify members details tab - search if fname already exist
# If so, add data to existing members tab. if not, create new tab
    WORKSHEET = SHEET.worksheet("members_details")
    existing_user_fnames = WORKSHEET.col_values(1)
    existing_user_lnames = WORKSHEET.col_values(2)
    existing_users = zip(existing_user_fnames, existing_user_lnames)

    if (
        fname not in existing_user_fnames
        or lname not in existing_user_lnames
        or (fname, lname) not in existing_users
    ):
        WORKSHEET = SHEET.worksheet("members_details")
        WORKSHEET.append_row([fname] + [lname])
        SHEET.add_worksheet(f"{fname}{lname}", 53, 20)

        if (
            fname not in existing_user_fnames
            or lname not in existing_user_lnames
        ):
            user_worksheet = SHEET.worksheet(f"{fname}{lname}")
            user_worksheet.update(
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

    welcome_message(fname)

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
                run_kms = float(answer)
                if run_kms < 0:
                    answer = input("Please try again: \n")
                    continue
                break
            except ValueError as e:
                answer = input(f"{e}: {answer} is not a number! Try Again: \n")
        user_answers.append(float(answer))

    print(f"you have entered: {user_answers}\n")

# calculate total weekly distance run
    sums = user_answers
    print(f"Your total distance this week is: {sum(sums)}kms \n")

    update_distance_log(user_answers, fname, lname)


# prompt user if they'd like to provide a weekly distance target
    while True:
        weekly_target = input("Would you like to provide a weekly target? y/n: \n")
        if weekly_target == "y":
            last_target = SHEET.worksheet(f"{fname}{lname}").acell("H2").value
            print(f"Your last Target was: {last_target} km \n")
            weekly_target = input("How many KMs do you plan to run next week?\n")
            while not weekly_target.isdigit():
                weekly_target = input("Error: please provide a distance in numerical form. \n")
            break
        if weekly_target =="n":
            print(f"OK {fname} Let's move on...\n")
            break        
        elif weekly_target != "y" or "n":
            print("Invalid answer. Please type y or n: \n")
            continue
        

# Prompt user if they'd like to calculate BMI and reveal calculated result
    while True:
        bmi_data = input(f"{fname} Would you like to know your BMI? y/n: \n")
        if bmi_data == "y":
            height = input("Please enter your current height in cm: \n")
            while not height.integer():
                height = input("Invalid response. Please provide your answer in numerical form. \n")

            weight = int(input("Please enter your current weight in kg: \n"))
            # while not weight.isdigit():
                # weight = input("Invalid response. Please provide your answer in numerical form. \n")
            bmi = weight/height/height*10000   
            print(f"Your BMI is: {bmi}")
            break            
        elif bmi_data == "n":
            print(f"OK {fname} Let's move on...\n")
            break
        else:
            bmi_data != "y" or "n"
            print("Invalid answer. Please type y or n: \n")

    
    bmi_info = input(
        "Want to know more about BMI & how it's calculated? y/n \n")
    if bmi_info == "n":
            print(f"OK {fname} Let's move on...\n")
    elif bmi_info == "y":
        print("https://www.truthaboutweight.global/\n")
    elif bmi_data != "y" or "n":
        print("Invalid answer. Please type y or n: \n")
            
        update_other_data(weekly_target, fname, lname, bmi_data)


if __name__ == "__main__":
    main()
