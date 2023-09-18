import sys
import random

# Define the main function
def main():
    # Get the user's account number
    account_number = input("Please Enter your account number: ")

    # Get the user's PIN
    pin = input("please Enter your PIN: ")

    # Check if the account number and PIN are correct
    if account_number == "1234567890" and pin == "1234":
        # Display the main menu
        print("Welcome to the ATM! Please select an option from the menu below:")

        # Get the user's selection
        selection = input("Selection: ")

        # Check the user's selection
        if selection == "1":
            # Withdraw money
            amount = input("please Enter the amount you would like to withdraw: ")
            if amount <= 10000:
              print("Withdrawal successful! Your new balance is:")
            else:
                print("Withdrawal failed! Please enter a smaller amount.")
        elif selection == "2":
            # Deposit money
            amount = input("Enter the amount you would like to deposit: ")
            print("Deposit successful! Your new balance is: ")

        elif selection == "3":
            # Check balance
            print("Your current balance is: ")

        elif selection == "4":
            # Exit
            print("Thank you for using the ATM!")
            sys.exit(0)

        else:
            print("Invalid selection! Please select a valid option.")

    else:
        print("Incorrect account number or PIN.")

# Call the main function
main()