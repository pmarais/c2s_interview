Click2Sure Techical interview
==============================

Get started with this repository

1. Create a python3 virtualenvironmnet with `virtualenv --python python3 _venv/`
2. Activate the virtualenvironment with `source _venv/bin/activate`
3. Install requirements: `pip install -r 017_click2sure/requirements.txt`
4. Move to the main app directory `click2sure_bank/`
4. Create the database and models `./manage.py migrate`
4. Create a user with `./manage.py createsuperuser` 
5. Enter the shell environment `./manage.py shell`
6. Run the contents of the helper file `from main.helpers import *`
7. Run the server `./manage.py runserver`
8. Visit http://localhost:8000/api/accounts/ and you should see a list of created accounts
9. Visit http://localhost:8000/api/users/ and you should see a list of created users
10. Visit http://localhost:8000/api/transactions/ and you should see a list of created transactions
11. Visit http://localhost:8000/api/myaccounts/ and you should see `"detail": "Authentication credentials were not provided."`
12. Visit http://localhost:8000/admin/ and login with the account you created
13. Visit http://localhost:8000/api/myaccounts/ and you should see your accounts (although it is the same as the 'all accounts')
14. You should be able to add a new transaction at http://localhost:8000/api/transactions/ adding values for all fields, but leaving the `tr_hash` field blank
