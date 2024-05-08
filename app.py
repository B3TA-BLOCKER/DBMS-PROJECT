from flask import Flask, render_template,request, redirect, url_for
import psycopg2
from config import config

app = Flask(__name__)

def connect():
    connection = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

# routing the application
@app.route("/")
def application():
  return render_template('login.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    if request.method == 'POST':
        # Perform some action when the button is clicked
        print("Button clicked!")
        # You can add more actions here, such as updating a database, sending a notification, etc.
    return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
