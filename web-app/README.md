# AlexaForInstructions

### How to run the app locally:
1. Navigate to the directory AlexaForInstructions/web-app in a terminal.
2. Enter the following:
```
$ run python.py
```

### Requirements to run the app locally:
1. Install dependencies using pip. The ones shown are the only ones necessary at the moment for database/login/register to work.
```
$ pip install flask pymysql validate_email
```
2. Install MySQL developer tools from the MYSQL installer [found here](https://dev.mysql.com/downloads/installer/). Follow the GUI's instructions to set
3. Use MySQL workbench to connect to your root MySQL instance (you should have set this up in the previous step).
4. Use MySQL workbench or terminal to instantiate the schema file found at AlexaForInstructions/web-app/schema.sql. You can just copy and paste the code, and then click the lightning bolt.

### Requirements to run the app on AWS server space:
1. ?
