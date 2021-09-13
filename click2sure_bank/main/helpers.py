from main.models import *

user = User.objects.all()[0]

acc1 = Account.objects.create(acc_user=user, acc_type='CRT')
acc1.uuid_generate()

acc1.open_account()
acc1.withdraw(withdraw_value=101000)
acc1.deposit(dep_value=2000)
acc1.withdraw(withdraw_value=101000)


acc2 = Account.objects.create(acc_user=user, acc_type='SVG')
acc2.uuid_generate()

# acc.deposit(dep_value=50)
acc2.open_account(dep_value=1000)
acc2.deposit(dep_value=5330)

acc2.withdraw(withdraw_value=75)
acc2.withdraw(withdraw_value=35)