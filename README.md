# githubstarsV1.1
Project description:
The githubstarsV1.1 app is an example RESTful web application developed in Python
using the Flask framework. The app connects to the Github API to read the json data
for the Python repositories which have the most stars. This data is then stored in a MySQL
database instance and displayed as a list.
Minimum Software Requirements:
Windows 7
Flask V 1.1
Python V 3.8.2
MySQL Database V 8.0
Instructions for DB access:
Step 1: Open the settings/config.ini file and provide the MySQL DB connection parameters needed for the application to run successfully. Please specify a root/admin account in MySQL so that the application connects and has the full read/write privileges to create the Database schema (github) and the table (repos) upon start up.
Step 2: Start the MySQL database server 
Step 3: Open the MySQL shell and type in these commands:
MySQL> \sql (press enter)
MySQL> \connect root@localhost (press enter)
Step 4: Download the githubstarsV1.1.zip from https://github.com/MaliniRaja/githubstarsV1.1
Step 5: Unzip the folder into your python workspace. The executable file to start the application is main.py. Open the project in PyCharm IDE (or your IDE of choice) to see the subfolders and code.
Step 6: To run the Flask application, make sure the libraries imported into the main.py file have been installed in your environment using pip. Example: “pip install flask as Flask”. Install the following packages: Json, urllib.request, Flask, flask_mysqldb configparser
Step7: To run the application, right-click the githubstarsV1.1/main.py file and click on run
Application design:
The database github contains 1 table called repos. As there is a one to one relationship between the list of the repositories and its details, all the data is stored in the same table.
The github/repos tables structure is as follows:
Field Name	Type	Null	Key	Default  
repo_id	int	NO	PK	NULL
name	varchar (100)	YES		NULL
url	varchar (1000)	YES		NULL
created_at	varchar (45)	YES		NULL
pushed_at	varchar (45)	YES		NULL
description	longtext	YES		NULL
num_stars	int	YES		NULL


Resources:
https://developer.github.vom/v3
https://developer.github.vom/v3/search
https://flask.palletsprojects.com/en/1.1.x/
https://www.python.org/download/releases/3.0/

