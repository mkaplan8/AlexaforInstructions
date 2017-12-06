# A4I Release Notes
Version 1.0

1. Web Application Features
```
    1. Users can create and login an account
    2. Users can upload an instruction set manually using the upload
    3. Users can upload an instruction set via file upload
    4. Users can flag uploads as either public or private
    5. Users can see their upload history and delete unnecessary uploads
```
2. Alexa Skill Features
```
    1. Users can ask Alexa to open an instruction set
    2. Users can use keywords like continue and previous to navigate through an instruction set
    3. Users can use advanced keywords such as skip to step {step number} to skip to a certain step number
    4. Users can use advanced keywords such as find {keyword} to skip to the first step with a certain word
    5. Users can use advanced keywords like save and wait to tell Alexa to pause the instruction set for a certain amount of time or to save the current step
```
3. Known Bug & Defects
```
    1. Alexa may not always completely understand what the user is saying
```

# A4I Installation Guide

## Visual Interface & Alexa Skill Installation

### Prerequisites and Dependencies
***You will need a computer device and access to the internet.***
1. Download and install Python 3.x.x from the link below. Follow the prompts.
```
    https://www.python.org/downloads/
```
2. Download get-pip.py from the link below.
```
    https://pip.pypa.io/en/stable/installing/
```
3. Open a new command terminal window to the folder where get-pip.py lies and install pip (Python Package Index).
```
    $ python get-pip.py
```
4. Install dependencies using pip.
```
    $ pip install flask flask-ask validate_email
```

5. Link the AlexaForInstructions amazon account to your Alexa enabled device.

### Build
1. Use the public Github link below to navigate to A4I's source code.
```
    https://github.com/mkaplan8/AlexaforInstructions
```
2. Click the green button labeled "Clone or download", and choose "Download ZIP".
3. Unzip the "AlexaforInstructions" folder to a locatable area.

### Run
1. Navigate to the directory AlexaForInstructions/web-app in a terminal.
2. Run the script named run.py using python.
```
    $ python run.py
        or
    $ ./run.py
```
3. Open up a web browser page to localhost address at port 5000.
```
    localhost:5000
```
---

## Audio Interface (Alexa-Skill)

### Prerequisites and Dependencies
***You will need an alexa enabled device with a internet connection.***
1. Navigate to directory /alexa_skill.
2. Download the correct distrubtion of ngrok for your operating system.
```
    $ https://ngrok.com/download
```
3. Run ngrok and note the https link in the output.
```
    $ ngrok http 5000
```
4. Run instructions.py.
```
    $ python instructions.py
```

### Run
1. Login to AlexaForInstructions Amazon developer account.
```
    https://developer.amazon.com
```

2. Navigate to the AlexaForInstructions skill configuration.

3. Enter the https link from step 2. into the default endpoint field.

4. Ask Alexa to 'open instructions guide'.
