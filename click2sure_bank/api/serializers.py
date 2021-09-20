## Serilizer classes
from rest_framework import serializers

from main.models import User, SavingsAccount, CurrentAccount, Transaction

##########
## User ##
##########
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

##############
## Accounts ##
##############
class SavingsAccountSerialiser(serializers.ModelSerializer):
    class Meta:
        model = SavingsAccount
        fields = '__all__'

#############
## Account ##
#############
class CurrentAccountSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CurrentAccount
        fields = '__all__'

# #############
# ## Account ##
# #############
# class CreateSavingsAccountSerialiser(serializers.ModelSerializer):
#     deposit_value = serializers.FloatField(write_only=True)
#     acc_comment = serializers.CharField(read_only=True, required=False)
#     # accounts = serializers.SerializerMethodField()

#     class Meta:
#         model = SavingsAccount
#         # fields = '__all__'
#         fields = ('deposit_value', 'acc_comment',
#          # 'accounts'
#          )

#     def create(self, validated_data):

#         try:

#             acc = SavingsAccount.objects.create(acc_user=self.context['request'].user, acc_type='SVG')
#             acc.uuid_generate()

#             ## open account with starting balance
#             acc.open_account(dep_value=validated_data['deposit_value'])
#             return {'acc_comment': "Created: %s"%acc}

#         except AssertionError as error:
#             print(error)
#             return {'acc_comment': error}
    
#     # def get_accounts(self, obj):
#     #     accounts = [acc.id for acc in self.context['request'].user.user_accounts.filter(acc_type='SVG')]
#     #     return accounts


#################
## Transaction ##
#################
class TransactionSerializer(serializers.ModelSerializer):
    tr_caccount = CurrentAccountSerialiser(read_only=True)
    tr_saccount = SavingsAccountSerialiser(read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

# class WithdrawSavingsAccountSerialiser(serializers.ModelSerializer):
#     withdraw_value = serializers.FloatField(write_only=True)
#     withdraw_response = serializers.CharField(read_only=True, required=False)
#     tr_account = AccountSerialiser(read_only=True)
#     withdraw_account_id = serializers.FloatField(write_only=True)

#     class Meta:
#         model = Transaction
#         # fields = '__all__'
#         fields = ('withdraw_value', 'withdraw_response', 'tr_account'
#          # 'accounts'
#          )

#     def create(self, validated_data):

#         try:

#             acc = Account.objects.get(acc_user=self.context['request'].user, acc_type='SVG')
#             acc.uuid_generate()

#             ## open account with starting balance
#             acc.open_account(dep_value=validated_data['deposit_value'])
#             return {'acc_comment': "Created: %s"%acc}

#         except AssertionError as error:
#             print(error)
#             return {'acc_comment': error}
    
#     # def get_accounts(self, obj):
#     #     accounts = [acc.id for acc in self.context['request'].user.user_accounts.filter(acc_type='SVG')]
#     #     return accounts



































