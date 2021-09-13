from django.test import TestCase

# Create your tests here.

from main.models import User, Account, Transaction

class AccountTestCase(TestCase):
	def setUp(self):
		user = User.objects.create(username='jj')
		acc = Account.objects.create(acc_user=user, acc_type='CRT')
		acc.uuid_generate()
		acc.open_account()
		acc.deposit(dep_value=2000)
		acc = Account.objects.create(acc_user=user, acc_type='SVG')
		acc.uuid_generate()
		acc.open_account(dep_value=5000)
		# acc.withdraw(withdraw_value=101000)

	def test_deposit_crt(self):
		acc = Account.objects.get(pk=1)
		self.assertEqual(acc.acc_balance, 2000)

	def test_deposit_cvg(self):
		acc = Account.objects.get(pk=2)
		acc.deposit(dep_value=2000)
		self.assertEqual(acc.acc_balance, 7000)

	def test_withdraw_crt(self):
		acc = Account.objects.get(pk=1)
		acc.withdraw(withdraw_value=101000)
		self.assertEqual(acc.acc_balance, -99000.0)

	def test_withdraw_svg(self):
		acc = Account.objects.get(pk=2)
		acc.withdraw(withdraw_value=3000)
		self.assertEqual(acc.acc_balance, 2000)
		