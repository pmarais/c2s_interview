#####################
## Account Service ##
#####################
## Import the required models iobjects
from main.models import *

if User.objects.all().count() == 0:
	User.objects.create_user(username='user1', email='user@space.com', first_name="first", last_name="last", password='this')

## Initiate an account service instance
## Specify a user PK number
accservice = AccountService(userid = 1)

## This should fail
# accservice.open_savings(account_id="One", ammount_to_deposit=100)

## This should work — Open a savings account
accservice.open_savings(account_id="One", ammount_to_deposit=1000)
accservice = AccountService(userid = 1)
accservice.deposit(account_id="One", ammount_to_deposit=50)

accservice = AccountService(userid = 1)
accservice.deposit(account_id="One", ammount_to_deposit=50)
accservice.deposit(account_id="One", ammount_to_deposit=50)

## Open a current account
accservice = AccountService(userid = 1)
accservice.open_current(account_id="Three")

## Withdraw
accservice = AccountService(userid = 1)
accservice.withdraw(account_id="Three", ammount_to_withdraw=30)


## Open another current account
accservice = AccountService(userid = 1)
accservice.open_current(account_id="Four", acc_overdraft_limit=30000)

## Open another current account
accservice = AccountService(userid = 1)
accservice.withdraw(account_id="Four", ammount_to_withdraw=30)


# #############
# ## Current ##
# #############
# ## Import the required models iobjects
# from main.models import *

# ## Select the first user in the list (which should be the only user, if you followed the instructions)
# user = User.objects.all()[0]

# ## Create a current account
# acc1 = CurrentAccount.objects.create(acc_user=user)
# ## Create a unique ID for account

# ## Run the model method to open the account
# ## The current account does not require a depost, so one is not specified
# acc1.open_account(dep_value=0, acc_overdraft_limit=100000)

# ## If run in sequence this will throw an AssertionError
# acc1.withdraw(withdraw_value=101000)

# ## Add a deposit
# acc1.deposit(dep_value=2000)

# ## Withdraw
# acc1.withdraw(withdraw_value=101000)


# #############
# ## Savings ##
# #############
# ## Import the required models iobjects
# from main.models import *

# ## Select the first user in the list (which should be the only user, if you followed the instructions)
# user = User.objects.all()[0]

# ## Create a savingsaccount
# acc2 = SavingsAccount.objects.create(acc_user=user)
# ## Create a unique ID for account
# acc2.uuid_generate()

# ## This will throw an assertion error if run in sequence
# acc2.deposit(dep_value=50)

# ## open account with starting balance
# acc2.open_account(dep_value=1000)
# ## Make a deposit
# acc2.deposit(dep_value=5330)

# ## Make withdrawals
# acc2.withdraw(withdraw_value=75)
# acc2.withdraw(withdraw_value=35)
















