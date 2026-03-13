import csv
from datetime import datetime

file_name = "users.csv"

def register_user():
    print("===== USER REGISTRATION =====")

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    country = input("Enter Country: ")

    # Read existing data to get next user ID
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            user_id = len(rows)
    except FileNotFoundError:
        user_id = 1

    reg_date = datetime.now().strftime("%Y-%m-%d")

    new_user = [user_id, first_name, last_name, email, username, password, country, reg_date]

    # Append new user
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_user)

    print("✅ Registration Successful!")

register_user()