import logging

from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, convert_errors

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def authentication():
    authentication_msg = render_template('authentication')
    return question(authentication_msg)

@ask.intent("PetIntent")
def which_account(pet):
    if pet != 'monkey':
        wrong = render_template('wrong')
        return statement(wrong)
    accounts = ['private account', 'student account', 'savings account']
    which_account_msg = render_template('accounts', accounts=accounts)
    return question(which_account_msg)

@ask.intent("AccountIntent")
def balance(account):
    balances = {
            'private account': 2321.10,
            'student account': 345.20,
            'savings account': 5045.30
            }
    account_balance_msg = render_template('balance', account=account, balance=balances[account] )
    return statement(account_balance_msg)

if __name__ == '__main__':
    app.run(debug=True)
