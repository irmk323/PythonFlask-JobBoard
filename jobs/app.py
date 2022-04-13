from flask import Flask, render_template, g 
import sqlite3

path = "db/jobs.sqlite"
app = Flask(__name__)


def open_connection():
  connection =  g.getattr('_connection')
  return connection

@app.route('/')
@app.route("/jobs")
def jobs():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()


