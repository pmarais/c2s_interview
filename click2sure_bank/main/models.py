from django.db import models
from django.contrib.auth.models import User

## For UUID generation
import uuid

# Create your models here.

class CurrentAccount(models.Model):
	acc_user = models.ForeignKey(User, related_name='user_current_accounts', on_delete=models.CASCADE, null=True, blank=True)
	acc_id = models.CharField(max_length=255, default='', blank=True, null=True)
	acc_balance = models.FloatField(null=True, blank=True, default=0)
	acc_created = models.DateTimeField(auto_now_add=True)
	acc_last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s) %s => R%s (\n%s)"%(self.pk, self.acc_user, self.acc_balance, self.acc_last_updated)

	def uuid_generate(self):
		"""
		Generating a unique ID
		"""
		self.acc_uuid = "%s"%(str(uuid.uuid4()))
		self.save()
		print("Created UUID for %s"%self)

	def open_account(self, dep_value=0):
		self.acc_balance = dep_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_caccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def deposit(self, dep_value):
		self.acc_balance += dep_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_caccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def withdraw(self, withdraw_value):
		assert (self.acc_balance - withdraw_value) >= -100000, "Overdraft limit is = R100,000. This transaction would result in a balance of R%s"%(self.acc_balance - withdraw_value)
		self.acc_balance -= withdraw_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_caccount=self, tr_type='WTD', tr_value=withdraw_value, tr_acc_balance_at=self.acc_balance)

class SavingsAccount(models.Model):
	acc_user = models.ForeignKey(User, related_name='user_savings_accounts', on_delete=models.CASCADE, null=True, blank=True)
	acc_id = models.CharField(max_length=255, default='', blank=True, null=True)
	acc_balance = models.FloatField(null=True, blank=True, default=0)
	acc_created = models.DateTimeField(auto_now_add=True)
	acc_last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s) %s => R%s (\n%s)"%(self.pk, self.acc_user, self.acc_balance, self.acc_last_updated)

	def uuid_generate(self):
		"""
		Generating a unique ID
		"""
		self.acc_uuid = "%s"%(str(uuid.uuid4()))
		self.save()
		print("Created UUID for %s"%self)

	def open_account(self, dep_value=0):
		assert dep_value >= 1000, "Initial Deposit value has to be ≥ R1,000."
		self.acc_balance = dep_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_saccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def deposit(self, dep_value):
		assert self.acc_balance >= 1000, "Balance needs to be R1,000 or more"
		self.acc_balance += dep_value
		self.save()
		tr = Transaction.objects.create(tr_user=self.acc_user, tr_saccount=self, tr_type='DEP', tr_value=dep_value, tr_acc_balance_at=self.acc_balance)
		print(self.__str__, tr.__str__)

	def withdraw(self, withdraw_value):
		assert (self.acc_balance - withdraw_value) >= 1000, "Remaining balance after withdrawal needs to be ≥ R1,000. This transaction would result in a balance of R%s"%(self.acc_balance - withdraw_value)
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

























