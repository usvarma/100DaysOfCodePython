# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def split_bill():
    total_bill = float(input("What was the total bill?"))
    tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
    split_ways = int(input("How many people to split the bill?"))
    split_amount = round((total_bill * (1 + (tip_percent / 100.0)) / split_ways), 2)
    print(f"Each person should pay: {split_amount}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the tip calculator")
    split_bill()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
