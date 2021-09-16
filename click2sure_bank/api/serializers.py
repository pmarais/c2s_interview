## Serilizer classes
from rest_framework import serializers

from main.models import User, Account, Transaction

##########
## User ##
##########
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#############
## Account ##
#############
class AccountSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

#############
## Account ##
#############
class CreateSavingsAccountSerialiser(serializers.ModelSerializer):
    deposit_value = serializers.FloatField(write_only=True)
    acc_comment = serializers.CharField(read_only=True, required=False)
    # accounts = serializers.SerializerMethodField()

    class Meta:
        model = Account
        # fields = '__all__'
        fields = ('deposit_value', 'acc_comment',
         # 'accounts'
         )

    def create(self, validated_data):

        try:

            acc = Account.objects.create(acc_user=self.context['request'].user, acc_type='SVG')
            acc.uuid_generate()

            ## open account with starting balance
            acc.open_account(dep_value=validated_data['deposit_value'])
            return {'acc_comment': "Created: %s"%acc}

        except AssertionError as error:
            print(error)
            return {'acc_comment': error}
    
    # def get_accounts(self, obj):
    #     accounts = [acc.id for acc in self.context['request'].user.user_accounts.filter(acc_type='SVG')]
    #     return accounts






#################
## Transaction ##
#################
class TransactionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
