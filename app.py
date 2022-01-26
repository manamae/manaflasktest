from flask import Flask, render_template, redirect, request, session,Response
# import mysql.connector
import psycopg2


app = Flask(__name__)

conn = psycopg2.connect(
	host = "ec2-54-157-16-125.compute-1.amazonaws.com",
	user = "znwahnrdcbtjjb",
	password = "a3b7b147ad6cbc9a3b07b51f02b9c96ca4d510607202f242706f54b255d58b2a",
	database = "d9mvoqrjshij7o"
)
conn.autocommit = True

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/db", methods = ['POST', 'GET'])
def db():
	x = "not connected"
	result = "nothing"
	if request.method == 'GET':
		if(conn):
			cursor = conn.cursor()
			# cursor.execute("SELECT * from test")
			cursor.execute("SELECT * from test")
			result = cursor.fetchall()
			x = "connected"
		return render_template("db.html",c = x,data = result)

	if request.method == 'POST':
		values = request.form.to_dict()
		val = values["val"]
		cursor = conn.cursor()
		# q = "ALTER TABLE test ADD COLUMN ID SERIAL PRIMARY KEY;;"
		# q = "ALTER TABLE test DROP COLUMN id;"
		# cursor.execute(q)
		q = "INSERT INTO TEST (name) VALUES (%s)"
		cursor.execute(q,(val,))
		conn.commit()

		return redirect("/db")
	

if __name__ == '__main__':
	app.run(debug=True,port=7890)