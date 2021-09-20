## Import the required models iobjects
from main.models import *

## Select the first user in the list (which should be the only user, if you followed the instructions)
user = User.objects.all()[0]

## Create a current account
acc1 = CurrentAccount.objects.create(acc_user=user)
## Create a unique ID for account
acc1.uuid_generate()

## Run the model method to open the account
## The current account does not require a depost, so one is not specified
acc1.open_account(dep_value=0, acc_overdraft_limit=100000)

## If run in sequence this will throw an AssertionError
acc1.withdraw(withdraw_value=101000)

## Add a deposit
acc1.deposit(dep_value=2000)

## Withdraw
acc1.withdraw(withdraw_value=101000)


#############
## Savings ##
#############
## Import the required models iobjects
from main.models import *

## Select the first user in the list (which should be the only user, if you followed the instructions)
user = User.objects.all()[0]

## Create a savingsaccount
acc2 = SavingsAccount.objects.create(acc_user=user)
## Create a unique ID for account
acc2.uuid_generate()

## This will throw an assertion error if run in sequence
acc2.deposit(dep_value=50)

## open account with starting balance
acc2.open_account(dep_value=1000)
## Make a deposit
acc2.deposit(dep_value=5330)

## Make withdrawals
acc2.withdraw(withdraw_value=75)
acc2.withdraw(withdraw_value=35)