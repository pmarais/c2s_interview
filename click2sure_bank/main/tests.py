from django.test import TestCase

# Create your tests here.

from main.models import *

class AccountTestCase(TestCase):
	def setUp(self):
		user = User.objects.create(username='jj')
		accservice = AccountService(userid = 1)
		accservice.open_savings(account_id="One", ammount_to_deposit=1200)
		accservice.open_current(account_id="Two", acc_overdraft_limit=30000)

	def test_savings_deposit(self):
		accservice = AccountService(userid = 1)
		accservice.deposit(account_id="One", ammount_to_deposit=50)

	def test_savings_withdraw(self):
		accservice = AccountService(userid = 1)
		accservice.withdraw(account_id="One", ammount_to_withdraw=100)

	def test_current_deposit(self):
		accservice = AccountService(userid = 1)
		accservice.deposit(account_id="Two", ammount_to_deposit=50)

	def test_savings_withdraw(self):
		accservice = AccountService(userid = 1)
		accservice.withdraw(account_id="Two", ammount_to_withdraw=100)
		accservice.withdraw(account_id="Two", ammount_to_withdraw=1000)
		accservice.withdraw(account_id="Two", ammount_to_withdraw=10000)

	# def test_deposit_crt(self):
	# 	acc = Account.objects.get(pk=1)
	# 	self.assertEqual(acc.acc_balance, 2000)

	# def test_deposit_cvg(self):
	# 	acc = Account.objects.get(pk=2)
	# 	acc.deposit(dep_value=2000)
	# 	self.assertEqual(acc.acc_balance, 7000)

	# def test_withdraw_crt(self):
	# 	acc = Account.objects.get(pk=1)
	# 	acc.withdraw(withdraw_value=101000)
	# 	self.assertEqual(acc.acc_balance, -99000.0)

	# def test_withdraw_svg(self):
	# 	acc = Account.objects.get(pk=2)
	# 	acc.withdraw(withdraw_value=3000)
	# 	self.assertEqual(acc.acc_balance, 2000)
		