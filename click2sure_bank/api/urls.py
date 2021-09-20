
from django.conf.urls import url

## For getting an API token from username and password for a user
from rest_framework.authtoken import views as api_auth_views

from . import views

## for anaytics urls
# from api.analytics import urls as _an_urls

app_name = 'api'

## Using python generic_views
## Note changed regex from question_id --> pk
urlpatterns = [

    ## Users
    url(r'^users/$', views.UserListiew.as_view(), name='users'),
    url(r'^savings_accounts/$', views.SavingsAccountListiew.as_view(), name='savings_accounts'),
    url(r'^current_accounts/$', views.CurrentAccountListiew.as_view(), name='current_accounts'),
    url(r'^my_savings_accounts/$', views.MySavingsAccountListiew.as_view(), name='my_savings_accounts'),
    # url(r'^create_savings_account/$', views.CreateSavingsAccountView.as_view(), name='create_savings_account'),
    # url(r'^withdraw_savings_account/$', views.WithdrawSavingsAccountView.as_view(), name='withdraw_savings_account'),
    url(r'^transactions/$', views.TransactionListiew.as_view(), name='transactions'),
    # url(r'^savings_account_withdraw/(?P<pk>[0-9]+)/$', views.SavingsAccountWithdraw.as_view(),  name="savings_account_withdraw"),

]
    