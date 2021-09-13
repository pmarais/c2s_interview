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


#################
## Transaction ##
#################
class TransactionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
