import logging

from random import randint
from flask import Flask, render_template, g
from flask_ask import Ask, statement, question, session
import json
import sqlite3

DATABASE = 'tasks.db'

instructions = []
place, end = 0,0

#Setup tasks database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#Open hard-coded example for demo purposes. This will replaced with query() later
f = open('example.json')
raw = f.read()
global j
j = json.loads(raw)

#Fetch instruction set from database
#def get_instructions(task):
    #Query sqlite3 db

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#initialize global vars and greet user
@ask.launch
def welcome():
    global place, end, instructions
    place, end = 0,0
    instructions = []
    cur = get_db()
    welcome_msg = render_template('welcome')
    reprompt_msg = render_template('reprompt')
    return question(welcome_msg).reprompt(reprompt_msg)
    
#task_name  parameter is the name of the task.
#supp parameter is supplies array from the task JSON.
def populate_instructions(task_name, supp, steps):
    msg = 'Here\'s how to {}. You will need'.format(task_name)
    for s in supp:
        msg = msg + ' ' + s['amount'] + ' ' + s['name'] + ','
    global instructions
    instructions.append(msg)
    for s in steps:
        instructions.append('step {},'.format(steps.index(s) + 1) + ' ' + s)
    global end
    end = len(steps)
    
#This method is used to query our task database
@ask.intent('QueryIntent')
def query(task):
    #First, transform our argument
    task = task.lower()
    task = task.replace('-', ' ')
    
    #find JSON in database and store in result. Store None if not found.
    statement = 'SELECT * FROM tasks where name="%s"'

    #execute statement and store in result
    cur = get_db()
    try:
        result = cur.execute(statement % (task))
        result = result.fetchall()
        print('result: {}'.format(result))
    except sqlite3.OperationalError:
        result = None
    #print('result: {}'.format(result))
    if len(result) > 0:
        populate_instructions(j['name'],j['supplies'],j['steps'])
        msg = 'I found the instructions. Say continue when ready.'
    else:
        msg = 'I could not find the instructions. Please try another query.'
    return question(msg)

#The user will iterate through instructions once the global instructions variable is populated.
@ask.intent('ContinueIntent')
def continue_task():
    global place
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    if place < end:
        #global place
        place += 1
        return question(instructions[place - 1])
    elif place == end:
        place += 1
        return question(instructions[end] + '. ' + 'This completes your task.')
    else:
        return welcome()
    
@ask.intent('PreviousIntent')
def prev_step():
    global place
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    if 0 < place <= end:
        place -= 1
        return question(instructions[place - 1])

@ask.intent('RepeatIntent')
def repeat_step():
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    else:
        return question(instructions[place - 1])
    
@ask.intent('JumpIntent')
def jump(number):
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    else:
        global place
        place = number
        return continue_task()
        
    
@ask.intent('AMAZON.StopIntent')
def stop():
    return statement('goodbye.')
    
@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
