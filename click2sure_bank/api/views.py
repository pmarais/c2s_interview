from django.shortcuts import render, get_object_or_404

from main.models import User, Transaction, SavingsAccount, CurrentAccount

## For permissions
from rest_framework import generics, permissions

## import serializers
from .serializers import UserSerializer, SavingsAccountSerialiser, TransactionSerializer

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

import json

class UserListiew(generics.ListAPIView):
    model = User
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer
    permission_classes =  (permissions.AllowAny,)

class SavingsAccountListiew(generics.ListAPIView):
    model = SavingsAccount
    queryset = SavingsAccount.objects.all().order_by('-pk')
    serializer_class = SavingsAccountSerialiser
    permission_classes =  (permissions.AllowAny,)

class CurrentAccountListiew(generics.ListAPIView):
    model = CurrentAccount
    queryset = CurrentAccount.objects.all().order_by('-pk')
    serializer_class = SavingsAccountSerialiser
    permission_classes =  (permissions.AllowAny,)

class MySavingsAccountListiew(generics.ListAPIView):
    model = SavingsAccount
    queryset = SavingsAccount.objects.all().order_by('-pk')
    serializer_class = SavingsAccountSerialiser
    permission_classes =  (permissions.IsAuthenticated,)

    def get_queryset(self):
        return SavingsAccount.objects.filter(acc_user__pk=self.request.user.pk)

# class CreateSavingsAccountView(generics.CreateAPIView):
#     model = SavingsAccount
#     queryset = SavingsAccount.objects.all().order_by('-pk')
#     serializer_class = CreateSavingsAccountSerialiser
#     permission_classes = (permissions.IsAuthenticated,)

# class WithdrawSavingsAccountView(generics.ListCreateAPIView):
#     model = Transaction
#     queryset = Transaction.objects.all().order_by('-pk')
#     serializer_class = WithdrawSavingsAccountSerialiser
#     permission_classes = (permissions.IsAuthenticated,)

#     def get_queryset(self):
#         return [Transaction.objects.filter(tr_user__pk=self.request.user.pk, tr_account__acc_type="SVG").last()]
#         # return Account.objects.filter(acc_user__pk=self.request.user.pk, acc_type="SVG")

# class SavingsAccountWithdraw(APIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (permissions.AllowAny,)

#     def get(self, request, **kwargs):
#         acc = get_object_or_404(SavingsAccount, pk=self.kwargs['pk'])
#         content = AccountSerialiser(acc).data
#         return Response(content)

#     def post(self, request, **kwargs):
#         if request.method == 'POST':
#             try:
#                 ## "{'withdraw_value':30}"
#                 ## curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/savings_account_withdraw/38/ -d "{'withdraw_value':30}"

#                 acc_id = self.kwargs['pk']
#                 print("Here ===>", acc_id)
#                 # withdraw_value = request.data['withdraw_value']
#                 print(request.data)
                
#                 # print("Here ===>", acc_id, withdraw_value)
                
#                 # acc = get_object_or_404(Account, pk=acc_id)
                
#                 # print(acc)


#             except:
#                 return Response("Failure")    
#             return Response("Success")
#         else:
#             return Response('Invalid POST', status=status.HTTP_400_BAD_REQUEST)

#         # iUA = InvestigateUserActivity(user)
#         # # iUA.action_print(iUA.important_actions)
#         # action_table = iUA.convert_to_action_table()
#         # responseObj = {
#         #     "results": action_table,
#         #     "user"   : UserDetailGetSerializer(user).data
#         # }





class TransactionListiew(generics.ListCreateAPIView):
    model = Transaction
    queryset = Transaction.objects.all().order_by('-pk')
    serializer_class = TransactionSerializer
    permission_classes =  (permissions.AllowAny,)






