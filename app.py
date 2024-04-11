from flask import Flask, render_template
import pypyodbc

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the MS Access database
    conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path_to_your_database.accdb;')
    cursor = conn.cursor()

    # Execute a sample query
    cursor.execute('SELECT * FROM YourTableName')
    data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
