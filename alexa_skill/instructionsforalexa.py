import logging
from random import randint
from flask import Flask, render_template, g
from flask_ask import Ask, statement, question, session
import json
import sqlite3
import time as t

#initialize global variables
DATABASE = 'tasks.db'
instructions = []
place, end = 0,0

#flask and logging stuff
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#Setup connection to tasks database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@ask.launch
def welcome():
    """
    This is the launch intent. Called when a user asks alexa to (launch/start/open...etc) instructions

    returns: (question) Our welcome message with reprompt if needed.
    """
    global place, end, instructions
    if (place, end) != (0, 0) and instructions != []:
        welcome_msg = render_template('old_session')
    else:
        place, end = 0,0
        instructions = [] #These first three lines may be redundant
        welcome_msg = render_template('welcome')
    cur = get_db()
    reprompt_msg = render_template('reprompt')
    return question(welcome_msg).reprompt(reprompt_msg)


def populate_instructions(task_name, supp, steps):
    """
    Helper function that fetches our task from DATABASE. Populates the global instructions variable.

    params
        task_name: (str) the name of the task
        supp: (list of dictionaries) This is a variable which represents all our supplies for our task.
        steps: (list of str) This parameter is a list of instructions for our task

    returns
        None
    """
    msg = 'Here\'s how to {}. You will need'.format(task_name)
    for s in supp:
        msg = msg + ' ' + s['amount'] + ' ' + s['name'] + ','
    global instructions
    instructions.append(msg)
    for s in steps:
        instructions.append('step {},'.format(steps.index(s) + 1) + ' ' + s)
    global end
    end = len(steps)

@ask.intent('QueryIntent')
def query(task):
    """
    This method is used to query our task database when a user asks for a task. Called on Alexa 'QueryIntent.'

    params
        task: (str) This is the task you ask alexa about

    returns
        msg: (question) This is the message alexa reads back to you.

    """
    #First, transform our argument
    task = task.lower()
    task = task.replace('-', ' ')

    print('task: {}'.format(task))

    #find JSON in database and store in result. Store None if not found.
    statement = 'SELECT * FROM tasks where name="%s"'

    #execute statement and store in result
    cur = get_db()
    try:
        result = cur.execute(statement % (task))
        result = result.fetchall()
    except sqlite3.OperationalError:
        result = None
    if len(result) > 0:
        populate_instructions(result[0][0], json.loads(result[0][1]), json.loads(result[0][2]))
        msg = 'I found the instructions. Say continue when ready.'
    else:
        msg = 'I could not find the instructions. Please try another query.'
    return question(msg)

@ask.intent('ContinueIntent')
def continue_task():
    """
    The user will use this function to iterate through instructions once the global instructions variable is populated.
    Called on Alexa 'ContinueIntent'

    returns
        msg: (str) The next step in instructions
    """
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
    """
    The user will use this function to iterate backwards through instructions once the global instructions variable is populated.
    Called on Alexa 'PreviousIntent'

    returns
        msg: (str) The previous step in instructions
    """
    global place
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    if 0 < place <= end:
        place -= 1
        return question(instructions[place - 1])

@ask.intent('RepeatIntent')
def repeat_step():
    """
    The user will use this function to repeat instructions once the global instructions variable is populated.
    Called on Alexa 'RepeatIntent'

    returns
    msg: (str) The current step in instructions
    """
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    else:
        return question(instructions[place - 1])

@ask.intent('JumpIntent')
def jump(number):
    """
    The user will use this function to jump to instructions once the global instructions variable is populated.
    Called on Alexa 'JumpIntent'

    returns
    msg: (str) The desired step in instructions
    """
    if len(instructions) == 0:
        return question('There is no current task session. What would you like me to do?')
    else:
        global place
        place = int(number)
        return continue_task()


@ask.intent('AMAZON.StopIntent')
def stop():
    """
    Stops the skill session. Called on Alexa 'StopIntent'

    returns
        msg: (statement) Goodbye message
    """
    global instructions, place, end
    instructions = []
    place, end = 0,0
    return statement('goodbye.')

@ask.intent('SaveIntent')
def save():
    """
    Stops the skill session, but saves the current session.

    returns
        msg: (statement) Goodbye message
    """
    return statement('Session Saved. Goodbye.')

@ask.intent('WaitIntent')
def wait(waitTime):
    """
    Tells the skill to wait (waitTIme) amount of time before repromting the user for an instructionco
    returns
    msg: (str) The current step after waiting for correct amount of time
    """

    waitTimeString = str(waitTime)
    time = ''
    interval = ''

    # time given was in seconds/minutes/hours
    if 'T' in waitTimeString:
        timeList = waitTimeString.split('T')
        totalTime = timeList[1]
        time = int(totalTime[:-1])
        interval = totalTime[len(totalTime) - 1:]

        # convert minutes to seconds
        if interval == 'M':
            time = time * 60
        # convert hours to seconds
        if interval == 'H':
            time = (time * 60) * 60

    t.sleep(time)
    return question('Continue to next step or repeat current step')

@ask.intent('SkipToWordIntent')
    """
    jumps to a step that has a certain keyword

    returns
        step that the word is in if word is in instructions
        msg: (statement) Make another word choice if word is not there
    """
def skipToWord(keyword):
    brokenDownInstruction = []
    instructionNumber = 0
    foundKeyWord = False
    keyword = keyword.upper()
    print keyword


    for instruction in instructions:
        # print 'current instruction: ' + str(instruction).upper()
        brokenDownInstruction = str(instruction).upper().split()
        for word in brokenDownInstruction:
            print word
            if word == keyword:
                foundKeyWord = True
                instructionNumber = brokenDownInstruction[1]
                instructionNumber = instructionNumber[:1]

    if foundKeyWord:
        return jump(int(instructionNumber))
    else:
        return statement('Could not find that word in the instructions, please try again')



@ask.session_ended
def session_ended():
    """
    Defines HTTP response for session end.

    returns
        "200 HTTP status code"
    """
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
