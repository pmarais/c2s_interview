from django.shortcuts import render
from main.models import User, Transaction, Account

## For permissions
from rest_framework import generics, permissions

## import serializers
from .serializers import UserSerializer, AccountSerialiser, TransactionSerialiser, CreateSavingsAccountSerialiser

# Create your views here.

class UserListiew(generics.ListAPIView):
    model = User
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer
    permission_classes =  (permissions.AllowAny,)

class AccountListiew(generics.ListAPIView):
    model = Account
    queryset = Account.objects.all().order_by('-pk')
    serializer_class = AccountSerialiser
    permission_classes =  (permissions.AllowAny,)

class MyAccountListiew(generics.ListAPIView):
    model = Account
    queryset = Account.objects.all().order_by('-pk')
    serializer_class = AccountSerialiser
    permission_classes =  (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Account.objects.filter(acc_user__pk=self.request.user.pk)

class CreateSavingsAccountView(generics.CreateAPIView):
    model = Account
    queryset = Account.objects.all().order_by('-pk')
    serializer_class = CreateSavingsAccountSerialiser
    permission_classes = (permissions.IsAuthenticated,)

class TransactionListiew(generics.ListCreateAPIView):
    model = Transaction
    queryset = Transaction.objects.all().order_by('-pk')
    serializer_class = TransactionSerialiser
    permission_classes =  (permissions.AllowAny,)