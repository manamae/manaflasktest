from flask import Flask, render_template, redirect, request, session,Response
import mysql.connector



app = Flask(__name__)

mydb = mysql.connector.connect(
	host = "ec2-54-157-16-125.compute-1.amazonaws.com",
	user = "znwahnrdcbtjjb",
	password = "a3b7b147ad6cbc9a3b07b51f02b9c96ca4d510607202f242706f54b255d58b2a",
	database = "d9mvoqrjshij7o"
)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/db", methods = ['POST', 'GET'])
def db():
	x = "not connected"
	if(mydb):
		x = "connected"
	return render_template("db.html",msg = x)
	# if request.method == 'GET':
	# 	mycursor = mydb.cursor()
	# 	return render_template("db.html",msg = "x")
	# if request.method == 'POST':
	# 	values = request.form.to_dict()
	

if __name__ == '__main__':
	app.run(debug=True,port=7890)