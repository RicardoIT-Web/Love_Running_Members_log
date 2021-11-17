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


def get_distance_run_data():
    """
    Recieve daily kms run from members.
    """
    print("Please provide the distance of your last run. ")
    print("You should provide this data in numerical form. ")
    print("Example: 3.2 = 3.2kms run. ")
    print("If you have not had a run today, please type 0.\n ")

    distance_str = input("Enter your kms here: ")
    print(f"The distance provided is {distance_str}kms")


get_distance_run_data()