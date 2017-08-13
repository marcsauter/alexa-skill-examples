# Alexa Skill Examples

## Links
### Adminstration
* [Amazon Developer Console](https://developer.amazon.com)
* [Amazon Alexa](https://alexa.amazon.com)
* [Amazon Alexa (de)](https://alexa.amazon.de)
* [History of your voice interactions with Alexa (Settings - History)](https://alexa.amazon.de/spa/index.html?#settings/dialogs)
* [Voice Training](https://www.amazon.com/gp/help/customer/display.html?nodeId=201601940)

### Fun
* [List of known easter eggs for Amazon Echo (so far)](https://www.reddit.com/r/amazonecho/comments/2v15fx/list_of_known_easter_eggs_for_amazon_echo_so_far)

> "Alexa, what's the answer to life, the universe, and everything?"

> "Alexa, what are the laws of robotics?" compare her answer with <a href="https://en.wikipedia.org/wiki/Laws_of_robotics">Laws of robotics<a>

### Technical
* [Understanding How Users Interact with Skills](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/understanding-how-users-interact-with-skills)
* [Choosing the Invocation Name for a Custom Skill](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/choosing-the-invocation-name-for-an-alexa-skill)
* [Slot Type Reference](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference)

### Tutorial
* [Alexa Python Tutorial](https://developer.amazon.com/de/alexa-skills-kit/alexa-skill-quick-start-tutorial)
* [Build an Alexa Skill with Python and AWS Lambda](http://moduscreate.com/build-an-alexa-skill-with-python-and-aws-lambda)
* [Developing Alexa Skills (Training by Big Nerd Ranch)](https://developer.amazon.com/de/alexa-skills-kit/big-nerd-ranch)

### Flask Ask
* [Flask Ask Documentation](https://flask-ask.readthedocs.io/en/latest)
* [Flask-Ask: A New Python Framework for Rapid Alexa Skills Kit Development](https://developer.amazon.com/de/blogs/post/tx14r0iyygh3skt/flask-ask:-a-new-python-framework-for-rapid-alexa-skills-kit-development)

### ngrok
* [ngrok - Secure tunnels to localhost](https://ngrok.com)

## Examples
### Setup
* python 2.7.x
* flask-ask
```
# pip install flask-ask
... or ...
# pip2 install flask-ask
```

* ngrok
```
# ./ngrok http 5000

ngrok by @inconshreveable                                                                                                                                                                                                                                             (Ctrl+C to quit)

Session Status                online
Update                        update available (version 2.2.8, Ctrl-U to update)
Version                       2.2.4
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://d1c7b569.ngrok.io -> localhost:5000
Forwarding                    https://d1c7b569.ngrok.io -> localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              17      0       0.00    0.00    0.45    0.65

HTTP Requests
-------------

POST /                         200 OK
```

### Basic Interaction
<img src="https://rawgithub.com/marcsauter/alexa-skill-examples/master/images/interaction.svg">

### Account Balance
```
# cd account_balance
# python account_balance.py
```

All Account Balances are hard-coded. Here would be a request to your Account Services.

### Account Balance with pin
```
# cd account_balance_pin
# python account_balance_pin.py
```

Yout PIN is **1984**. The PIN is hard-coded.

### Account Balance with Security Question
```
# cd account_balance_pet
# python account_balance_pet.py
```

Your favorite pet is a **monkey**. The Answer is hard-coded.
