from django.db import models
from django.contrib.auth.models import User

## For UUID generation
import uuid

###################
## Custom Errors ##
###################
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class AccountNotFoundError(Error):
    """Raised when account not found"""
    pass


class WithdrawAmmountTooLarge(Error):
    """Raised when the withdraw ammount is too large"""
    pass

############
## Models ##
############

class CurrentAccount(models.Model):
	acc_user = models.ForeignKey(User, related_name='user_current_accounts', on_delete=models.CASCADE, null=True, blank=True)
	acc_id = models.CharField(max_length=255, default='', blank=True, null=True, unique=True)
	acc_balance = models.FloatField(null=True, blank=True, default=0)
	acc_created = models.DateTimeField(auto_now_add=True)
	acc_overdraft_limit = models.FloatField(null=True, blank=True, default=0)
	acc_last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "[%s] %s) %s => R%s (\n%s)"%(self.acc_id, self.pk, self.acc_user, self.acc_balance, self.acc_last_updated)

	def uuid_generate(self):
		"""
		Generating a unique ID
		"""
		self.acc_uuid = "%s"%(str(uuid.uuid4()))
		self.save()
		print("Created UUID for %s"%self)

	def open_account(self, acc_id="", dep_value=0, acc_overdraft_limit=0):
		if acc_overdraft_limit <= 100000:
			self.acc_balance = dep_value
			self.acc_overdraft_limit = acc_overdraft_limit
			self.acc_id = acc_id
			self.save()
			tr = Transaction.objects.create(tr_user=self.acc_user, tr_caccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
			print(self.__str__, tr.__str__)

	def deposit(self, dep_value):
		self.acc_balance += dep_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_caccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def withdraw(self, withdraw_value):
		if self.acc_balance - withdraw_value <= -self.acc_overdraft_limit:
			raise WithdrawAmmountTooLarge
		# assert (self.acc_balance - withdraw_value) >= -self.acc_overdraft_limit, "Overdraft limit is = %s. This transaction would result in a balance of R%s"%(self.acc_overdraft_limit, self.acc_balance - withdraw_value)
		self.acc_balance -= withdraw_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_caccount=self, tr_type='WTD', tr_value=withdraw_value, tr_acc_balance_at=self.acc_balance)
		print(tr)			


class SavingsAccount(models.Model):
	acc_user = models.ForeignKey(User, related_name='user_savings_accounts', on_delete=models.CASCADE, null=True, blank=True)
	acc_id = models.CharField(max_length=255, default='', blank=True, null=True)
	acc_balance = models.FloatField(null=True, blank=True, default=0)
	acc_created = models.DateTimeField(auto_now_add=True)
	acc_last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "[%s] %s) %s => R%s (\n%s)"%(self.acc_id, self.pk, self.acc_user, self.acc_balance, self.acc_last_updated)

	def uuid_generate(self):
		"""
		Generating a unique ID
		"""
		self.acc_uuid = "%s"%(str(uuid.uuid4()))
		self.save()
		print("Created UUID for %s"%self)

	def open_account(self, acc_id="", dep_value=0):
		assert dep_value >= 1000, "Initial Deposit value has to be ≥ R1,000."
		self.acc_balance = dep_value
		self.acc_id = acc_id
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_saccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def deposit(self, dep_value):
		assert self.acc_balance >= 1000, "Balance needs to be R1,000 or more at all times"
		self.acc_balance += dep_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_saccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def withdraw(self, withdraw_value):
		# assert (self.acc_balance - withdraw_value) >= 1000, "Remaining balance after withdrawal needs to be ≥ R1,000. This transaction would result in a balance of R%s"%(self.acc_balance - withdraw_value)
		if self.acc_balance - withdraw_value < 1000:
			raise WithdrawAmmountTooLarge
		self.acc_balance -= withdraw_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_saccount=self, tr_type='WTD', tr_value=withdraw_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

## Transactions
## The idea is to create a transaction with every deposit and withdrawal, doing so automatically as a model method above.
class Transaction(models.Model):
	tr_user = models.ForeignKey(User, related_name='user_transactions', on_delete=models.CASCADE, null=True, blank=True)
	tr_saccount = models.ForeignKey(SavingsAccount, related_name = 'savings_account_transactions', on_delete=models.CASCADE, null=True, blank=True)
	tr_caccount = models.ForeignKey(CurrentAccount, related_name = 'current_account_transactions', on_delete=models.CASCADE, null=True, blank=True)
	tr_acc_balance_at = models.FloatField(null=True, blank=True, default=0)
	tr_hash = models.CharField(max_length=10, default='', blank=True, null=True)
	tr_type = models.CharField(max_length=10, default='CRT', blank=True, null=True, choices=(('WTD', 'Withdrawal'),('DEP', 'Deposit')))
	tr_value = models.FloatField(null=True, blank=True)
	tr_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		if self.tr_saccount != None:
			account = self.tr_caccount
		else:
			account = self.tr_saccount
		return "%s) %s [%s] (account balance after this transactions = R%s): %s"%(self.pk, self.tr_type, self.tr_value, self.tr_acc_balance_at, account)





#####################
## Account service ##
#####################
class AccountService():

	def __init__(self, userid):
		self.user = User.objects.get(pk=userid)

	def open_savings(self, account_id, ammount_to_deposit):
		assert ammount_to_deposit >= 1000, "Initial deposit needs to be ≥ R1,000"
		acc = SavingsAccount.objects.create(acc_user=self.user)
		acc.open_account(acc_id=account_id, dep_value=ammount_to_deposit)

	def open_current(self, account_id, acc_overdraft_limit=20000):
		acc = CurrentAccount.objects.create(acc_user=self.user)
		acc.open_account(acc_id=account_id, acc_overdraft_limit=acc_overdraft_limit)

	def __get_account(self, account_id):
		acc = SavingsAccount.objects.filter(acc_id=account_id)
		if len(acc) == 0:
			acc = CurrentAccount.objects.filter(acc_id=account_id)
		if len(acc) == 0:
			raise AccountNotFoundError
		return acc[0]

	def deposit(self, account_id, ammount_to_deposit):
		acc = self.__get_account(account_id=account_id)
		if acc != None:
			acc.deposit(dep_value=ammount_to_deposit)
		

	def withdraw(self, account_id, ammount_to_withdraw):
		acc = self.__get_account(account_id=account_id)
		if acc != None:
			acc.withdraw(withdraw_value=ammount_to_withdraw)



















