# Welcome to your turnip farm
# Please select one of the following options:
# 1. Plant a seed
# 2. Harvest a turnip
# 3. View your turnips

# Output
# 1. You planted a seed
# 2. You harvested a turnip
# 3.1 You don't have any turnips. Plant and harvest turnips to view them here.
# 3.2 Your turnips: 1 / You have 1 turnips
# 4. (anything else) You goofball! Select 1 or 2 or 3 from the menu.

print("Welcome to your turnip farm!")

def create_menu():
    print("Enter 1 to plant a turnip")
    print("Enter 2 to harvest a turnip")
    print("Enter 3 to view your turnips")
    print("Enter 4 to leave your farm")

    user_choice = input("Enter your selection: ")
    return user_choice

print(create_menu())