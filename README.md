# Brobot

Sample code for a tutorial on bot creation in Python: <a href="https://apps.worldwritable.com/tutorials/chatbot">Chatbot Fundamentals:
An interactive guide to writing bots in Python</a>

## Installation

Requires Python 2.7 or Python 3

### Set up and activate a virtualenv

`python virtualenv venv`

`. venv/bin/activate`

### Install the Python-level dependencies

`pip install -r requirements.txt`

### Install NLTK corpora

`python -m textblob.download_corpora`

### Run the command-line interface

This script runs an endless loop. You can start it via calling:

`python broize.py `

Just type in whatever you prefer and chat with Brobot!
If you wish to end the chat, just type:

`quit`

Note that this bot is _extremely simple_ as it's been optimized for use
as a training tool. It's not very interesting by itself!


## License
Copyright (c) 2016 Liza Daly / Licensed under the MIT license.
