import sys

# -------------------------- DECLARE variables for balance, deposit, and withdrawal --------------------------

account_balance = float(500.25)                                                 # Starting balance indicated by Codio
deposit_amount = 0                                                              # Declare variable 'deposit_amount'
withdrawal_amount = 0                                                           # Declare variable 'withdrawal_amount'


# -------------------------- DEFINE FUNCTIONS - balance, withdrawal, and deposit -----------------------------

def balance(account_balance):                                                   # Define balance function
  print("Your current balance is $%.2f" % (account_balance))                    # Prints the current avalible balance

def deposit(account_balance, deposit_amount):                                   # Define DEPOSIT function with parameters account_balance and deposit_amount
  deposit_amount = float(input("How much would you like to deposit today?\n"))  # Accept user input for the deposit amount, in float format
  balance = account_balance + deposit_amount                            # This addition assigns the updated value of the account blance, to the variable 'BALANCE'
  print("Deposit was $%.2f , your new current balance is $%.2f" % (deposit_amount, balance))  # Prints depost amount and account balance

def withdrawal(account_balance, withdrawal_amount):                             # Define WITHDRAWAL function with parameters account_balance and withdrawal_amount
  withdrawal_amount = float(input("How much would you like to withdraw today?\n")) #  Accept user input for the withdrawal amount, in float format
  if withdrawal_amount > account_balance:                                       # Checking to see if the amount requested, is greater than the amount avalible
    print("Insuffient funds, $%.2f is greater than your account balance of $%.2f" % (withdrawal_amount, balance)) # If the amount requested is greater than the account balance, there are insuffient funds
  else:                                                                         # Suffient amount of funds are avalible, the function continues
    balance = account_balance - withdrawal_amount                               # Variable 'balance' is assigned to reflect the new avalible balance
    print ("Withdrawal amount was $%.2f, your new current balance is $%.2f" % (withdrawal_amount, balance))  # Prints withdrawal amount and account balance


# Lines 18 and 20 compose a conditional statement with the withdrawal function
# Line 18 => if the requested withdwal amount is greater than the account balance, the conditional statement stops, and prints to the user there are insuffient funds
# Line 20 => if there are Suffient funds avalible, the conditional statement continues, updates the 'balance', and outputs to the user their withdwal amount and new avalible balance

# ------------------------------------ ACCEPT USER INPUT - D, B, W, or Q -------------------------------------

# Step ONE =>  Ask user what action they would like to proceed with, user input is accepted and assigned to the variable 'userchoice'
userChoice = input ("Would you like to check your (B)alance, make a (D)eposit, (W)ithdraw cash, or (E)xit?\n").upper()

# Step TWO => conditional statement begins based on the value of variable 'userchoice' from user input
# Four branches ustilizing if / elif for DEPOSIT, BALANCE, WITHDRAWAL, EXIT
if (userChoice == 'D'):                                                         # Accepts input D and proceeds with function 'deposit'
  deposit (account_balance, deposit_amount)                                     # DEPOSIT function is called with parameters 'account_balance' and 'deposit_amount'

elif (userChoice == 'B'):                                                       # Accepts input B and proceeds with function 'balance'
  balance (account_balance)                                                     # BALANCE function is called with parameter 'account_balance'

elif (userChoice == 'W'):                                                       # Accepts input D and proceeds with function 'withdrawal'
  withdrawal (account_balance, withdrawal_amount)                               # WITHDRAWAL function is called with parameters 'account_balance' and 'withdrawal_amount'

elif (userChoice == 'E'):                                                       # Accepts input E for EXIT
  print("Thank you for banking with us.")                                       # EXIT ends the program, and therefore the user has a printed message ending their session
