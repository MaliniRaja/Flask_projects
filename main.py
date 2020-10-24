import json
from urllib.request import urlopen
from flask import Flask, render_template,redirect,request
from flask_mysqldb import MySQL
import configparser
app = Flask(__name__)

gitpage = urlopen('https://api.github.com/search/repositories?q=language:"Python"&sort=stargazers_count&order=desc')
json_contents = gitpage.read()
json_obj = json.loads(json_contents)
rowDict = json_obj['items']

# Read local file `config.ini`.
config = configparser.ConfigParser()
config.read('settings/config.ini')
# Get values from config.ini file
c_user=config.get('DATABASE', 'USERNAME')
c_pass=config.get('DATABASE', 'PASSWORD')
c_host=config.get('DATABASE', 'HOST')
c_port=config.get('DATABASE', 'PORT')

#connect to Mysql DB using the values from the config.ini file
app.config['MYSQL_HOST'] = c_host
app.config['MYSQL_PORT'] = int(c_port)
app.config['MYSQL_USER'] = c_user
app.config['MYSQL_PASSWORD'] = c_pass

mysql = MySQL(app)

#Main homepage
@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("set character set utf8mb4")
    cur.execute("set character_set_connection=utf8mb4")
    cur.execute(''' CREATE DATABASE IF NOT EXISTS github''')
    cur.execute(''' CREATE TABLE IF NOT EXISTS github.repos(repo_id INT NOT NULL PRIMARY KEY, name VARCHAR(100),
    url VARCHAR(1000), created_at VARCHAR(45),pushed_at VARCHAR (45), description
    VARCHAR(5000),num_stars INT)''')
    for i in range(len(rowDict)):
        cur.execute("""REPLACE into github.repos(repo_id,name,url,created_at,pushed_at,description,num_stars) VALUES(%s,
    %s,%s,%s,%s,%s,%s)""", ((str(rowDict[i]['id']), str(rowDict[i]['name']), str(rowDict[i]['html_url']),
                             str(rowDict[i]['created_at']), str(rowDict[i]['pushed_at']),
                             str(rowDict[i]['description']), str(rowDict[i]['stargazers_count'])
                             )))

    mysql.connection.commit()
    cur.close()
    return render_template('index.html')

#List of Python github accounts read from the DB
@app.route('/list',methods=['GET','POST'])
def list():

    cur = mysql.connection.cursor()
    resultValue = cur.execute("select * from github.repos order by num_stars desc")
    if resultValue > 0:
        listDetails = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('list.html', listDetails=listDetails)

@app.route('/listitem/<lid>', methods=['GET'])
def listitem(lid):
    cur = mysql.connection.cursor()
    sql_select_query = """select * from github.repos where repo_id = %s"""
    numResults=cur.execute(sql_select_query, (lid,))
    if numResults > 0:
        resultSet = cur.fetchall()
    else:
        return "NO DATA"
    mysql.connection.commit()
    cur.close()
    return render_template('listItem.html',resultSet=resultSet)


#List of Python github accounts read directly from the github api
@app.route("/repos")
def repos():
    total = json_obj['total_count']
    return render_template("topRepos.html", gitrepo=rowDict,total=total)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

if __name__ == "__main__":
    app.run(debug=True)
